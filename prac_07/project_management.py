import datetime
from project import Project

def load_projects(filename):
    projects = []
    try:
        with open(filename, 'r') as file:
            next(file)  # Skip the header line
            for line in file:
                fields = line.strip().split('\t')
                project = Project(*fields)
                projects.append(project)
    except FileNotFoundError:
        print("File not found.")
    return projects

def save_projects(filename, projects):
    with open(filename, 'w') as file:
        file.write("Name\tStart Date\tPriority\tCost Estimate\tCompletion Percentage\n")
        for project in projects:
            file.write(f"{project.name}\t{project.start_date.strftime('%d/%m/%Y')}\t"
                       f"{project.priority}\t{project.cost_estimate:.2f}\t{project.completion_percentage}\n")

def display_projects(projects):
    incomplete_projects = [project for project in projects if project.completion_percentage < 100]
    completed_projects = [project for project in projects if project.completion_percentage == 100]

    print("Incomplete projects:")
    for project in sorted(incomplete_projects, key=lambda x: x.priority):
        print(f"  {project}")

    print("Completed projects:")
    for project in sorted(completed_projects, key=lambda x: x.priority):
        print(f"  {project}")

def filter_projects_by_date(projects, date_str):
    try:
        filter_date = datetime.datetime.strptime(date_str, "%d/%m/%Y").date()
        filtered_projects = [project for project in projects if project.start_date > filter_date]
        for project in sorted(filtered_projects, key=lambda x: x.start_date):
            print(f"  {project}")
    except ValueError:
        print("Invalid date format. Use dd/mm/yyyy.")

def add_new_project(projects):
    print("Let's add a new project")
    name = input("Name: ")
    start_date_str = input("Start date (dd/mm/yyyy): ")
    priority = int(input("Priority: "))
    cost_estimate = float(input("Cost estimate: $"))
    completion_percentage = int(input("Percent complete: "))

    new_project = Project(name, start_date_str, priority, cost_estimate, completion_percentage)
    projects.append(new_project)
    print("New project added successfully.")

def update_project(projects):
    print("Choose a project to update:")
    for i, project in enumerate(projects):
        print(f"{i} {project}")

    choice = input("Project choice: ")
    try:
        choice = int(choice)
        if 0 <= choice < len(projects):
            project = projects[choice]
            new_completion = input("New Percentage: ")
            if new_completion:
                project.completion_percentage = int(new_completion)
            new_priority = input("New Priority: ")
            if new_priority:
                project.priority = int(new_priority)
            print(f"Project updated: {project.name}")
        else:
            print("Invalid choice.")
    except ValueError:
        print("Invalid choice. Enter a number.")

def main():
    projects = []
    filename = "projects.txt"

    while True:
        print("- (L)oad projects")
        print("- (S)ave projects")
        print("- (D)isplay projects")
        print("- (F)ilter projects by date")
        print("- (A)dd new project")
        print("- (U)pdate project")
        print("- (Q)uit")

        choice = input(">>> ").lower()

        if choice == 'l':
            projects = load_projects(filename)
            print("Projects loaded successfully.")
        elif choice == 's':
            save_projects(filename, projects)
            print("Projects saved successfully.")
        elif choice == 'd':
            display_projects(projects)
        elif choice == 'f':
            date_str = input("Show projects that start after date (dd/mm/yyyy): ")
            filter_projects_by_date(projects, date_str)
        elif choice == 'a':
            add_new_project(projects)
        elif choice == 'u':
            update_project(projects)
        elif choice == 'q':
            print("Thank you for using custom-built project management software.")
            break
        else:
            print("Invalid choice. Please select a valid option.")

if __name__ == "__main__":
    main()

