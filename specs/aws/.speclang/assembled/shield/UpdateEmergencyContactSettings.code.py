def handler(store, request):
    emergency_contact_list = request.get("EmergencyContactList")
    return store.update_emergency_contact_settings(emergency_contact_list=emergency_contact_list)
