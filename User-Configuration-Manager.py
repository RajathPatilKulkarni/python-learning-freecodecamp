def add_setting(settings, values):
    key, value = values
    k, v = key.lower(), value.lower()
    if k in (key for key in settings):
        return f"Setting '{k}' already exists! Cannot add a new setting with this name."
    settings[k] = v
    return f"Setting '{k}' added with value '{v}' successfully!"
    
def update_setting(settings, values):
    key, value = values
    k, v = key.lower(), value.lower()
    if k in (key for key in settings):
        settings[k] = v
        return f"Setting '{k}' updated to '{v}' successfully!"
    return f"Setting '{k}' does not exist! Cannot update a non-existing setting."

def delete_setting(settings, key):
    k = key.lower()
    if k in (key for key in settings):
        del settings[k]
        return f"Setting '{k}' deleted successfully!"
    return "Setting not found!"

def view_settings(settings):
    if not settings:
        return "No settings available."
    lines = [f"{key.capitalize()}: {value}" for key, value in settings.items()]
    settings_text = "\n".join(lines)
    return f"""Current User Settings:
{settings_text}\n"""

test_settings = {'theme': 'dark'}
