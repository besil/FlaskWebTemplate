import argparse
import os

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description="Init script")
    parser.add_argument("project_name", metavar="Project_Name", type=str, help="Project name")

    args = parser.parse_args()

    project_name = args.project_name

    os.rename("TemplateProject", project_name)
    os.remove("init.py")