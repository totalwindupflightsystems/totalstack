#!/usr/bin/env python3
"""Owl Thinker: Feed AWS specs to owl-alpha, capture reasoning, feed to codegen."""
import os
import sys
import json
import subprocess
from pathlib import Path

OPENROUTER_KEY = os.environ.get("OPENROUTER_API_KEY", "")
OPENROUTER_URL = "https://openrouter.ai/api/v1/chat/completions"

def call_owl(prompt: str, max_tokens: int = 4096) -> str:
    """Call owl-alpha via OpenRouter. Returns text response."""
    payload = {
        "model": "openrouter/owl-alpha",  # owl-alpha
        "messages": [{"role": "user", "content": prompt}],
        "max_tokens": max_tokens,
        "temperature": 0.3,
    }
    result = subprocess.run(
        ["curl", "-s", OPENROUTER_URL,
         "-H", f"Authorization: Bearer {OPENROUTER_KEY}",
         "-H", "Content-Type: application/json",
         "-d", json.dumps(payload)],
        capture_output=True, text=True, timeout=120
    )
    if result.returncode != 0:
        return f"[ERROR] curl failed: {result.stderr}"
    try:
        data = json.loads(result.stdout)
        return data["choices"][0]["message"]["content"]
    except (json.JSONDecodeError, KeyError) as e:
        return f"[ERROR] Parse failed: {e}\nRaw: {result.stdout[:500]}"

def read_spec(spec_path: str) -> str:
    """Read a spec file, resolve @ref: directives to include referenced content."""
    content = Path(spec_path).read_text()
    # Resolve @ref: paths (same directory)
    spec_dir = Path(spec_path).parent
    resolved = []
    for line in content.split("\n"):
        if line.strip().startswith("@ref:"):
            ref_path = line.strip().replace("@ref:", "").strip()
            ref_file = spec_dir / ref_path
            if ref_file.exists():
                ref_content = ref_file.read_text()
                resolved.append(f"\n## REFERENCED: {ref_path}\n{ref_content[:8000]}\n")
        else:
            resolved.append(line)
    return "\n".join(resolved)

def main():
    if len(sys.argv) < 2:
        print("Usage: owl-thinker.py <spec-file> [--output <file>]")
        sys.exit(1)

    spec_path = sys.argv[1]
    output_file = None
    if "--output" in sys.argv:
        idx = sys.argv.index("--output")
        output_file = sys.argv[idx + 1]

    # Read spec + resolved refs
    spec_content = read_spec(spec_path)
    spec_name = Path(spec_path).stem

    # Determine what kind of spec this is
    is_meta = ".spec.meta.md" in spec_path
    is_plan = ".spec.plan.md" in spec_path
    is_code = ".spec.py.md" in spec_path or ".spec.ts.md" in spec_path

    if is_meta:
        prompt = f"""You are an AWS architect. Analyze this service meta-spec and produce:

1. **Architecture Assessment** (3-5 bullets): strengths, gaps, risks
2. **Implementation Priority** (ranked list): which operations to build first and why
3. **Error Model Recommendations**: what error types need coverage
4. **Testing Strategy**: what integration + E2E scenarios are critical

META SPEC:
{spec_content[:30000]}

Be concise. Use bullet points. No markdown headers — just plain text with category labels."""
    elif is_plan:
        prompt = f"""You are an AWS service implementer. Review this implementation plan and produce:

1. **Gap Analysis**: what's missing from the plan
2. **Edge Cases**: what scenarios aren't covered
3. **Integration Points**: dependencies on other services
4. **Implementation Order**: suggested build sequence

PLAN SPEC:
{spec_content[:30000]}

Concise bullet points. Plain text."""
    elif is_code:
        prompt = f"""You are a code reviewer. Analyze this AWS service handler spec and produce:

1. **Completeness Check**: does it cover all input validation?
2. **Error Handling Gaps**: what error scenarios are missing?
3. **AWS Compliance**: does it match the documented AWS behavior?
4. **Suggested Improvements**: concrete changes

HANDLER SPEC:
{spec_content[:25000]}

Bullet points. Plain text."""
    else:
        prompt = f"Analyze this spec:\n{spec_content[:30000]}\nProvide recommendations."

    print(f"[owl-thinker] Analyzing {spec_name}...")
    result = call_owl(prompt)

    if output_file:
        Path(output_file).write_text(result)
        print(f"[owl-thinker] ✅ Output written to {output_file}")
    else:
        print("=== OWL-ALPHA ANALYSIS ===")
        print(result)
        print("=== END ===")

if __name__ == "__main__":
    main()
