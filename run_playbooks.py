from ansible_playbook_runner import Runner

def ansible_skill(incoming_msg):

    Runner(['./hosts'], './show_version.yaml').run()

    return "Command fully run. Check ./sh_ver_folder to see results!"