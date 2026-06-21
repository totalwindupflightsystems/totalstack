def handler(store, request):
    emergency_contact_list = request.get("EmergencyContactList")
    return store.associate_proactive_engagement_details(emergency_contact_list=emergency_contact_list)
