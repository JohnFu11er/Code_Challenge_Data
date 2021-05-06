Easy:

Create an ansible playbook that creates a directory called “my_ansible_files”. Next, create a file called “my_file.txt” inside the directory “my_ansible_files”.

 
Medium:

Perform the above easy task, but this time use a loop technique to create 10 files named “router_1.cfg” through “router_10.cfg” in the "my_ansible_files" folder.

 
Hard:

Create an ansible playbook that creates a folder named “job_applicants”. In this folder, use ansible to create files for each candidate that you are interviewing. The filenames will be the applicants first name and last name separated by an underscore (john_smith.txt). Each of these text files will contain the data for only one candidate as given below (make sure to use a jinja template):

        Candidate 1:
            First name: John
            Last name: Smith
            Age: 23
            Education level: Associates

        Candidate 2:
            First name: Susan
            Last name: Smith
            Age: 27
            Education level: Bachelors

        Candidate 3:
            First name: Aaron
            Last name: Franklin
            Age: 35
            Education level: Masters