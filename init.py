import argparse
import os
from subprocess import call

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description="Init script")
    parser.add_argument("project_name", metavar="Project_Name", type=str, help="Project name")

    args = parser.parse_args()

    project_name = args.project_name

    call("rm -rf .git", shell=True)
    call("rm LICENSE", shell=True)
    call("rm README.md", shell=True)
    call("cd TemplateProject/", shell=True)
    call("TemplateProject/webapp/static/lib; bash install_libs.sh", project_name)
    os.rename("TemplateProject", project_name)
    os.remove("init.py")