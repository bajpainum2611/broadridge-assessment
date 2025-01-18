# broadridge-assessment

#Docker-Compose DevOps task
This file is a setup for multi-service application using Docker compose file where our Frontend are on Nginx Services, a backend API , PostgreSql database , and volumne with Networks.

##Service Overview
--Frontend :  Nginx service , port map to 80:80 for host and container , volumes for serve static files.
--Backend :  Install dependencies , artifacts , configure Env variables , set CPU LIMIT.
--Database : Store value for username and password .
--Networking : Use custom network
--Volumes : persist data for Postgresql and store nginx static files.

##Instruction to Setup Project
1. --bash
   -git clone https://github.com/bajpainum2611/broadridge-assessment.git
   -cd \broadridge-assessment\docker-task
2. Now create Secrets and Environment Variables:

   -- Create a file called secrets/db_password.txt and add your database password.
   -- Set the DB_USER and DB_NAME environment variables in a .env file or directly in your shell.

   Example .env file:
   DATABASE_USER=myuser
   DATABASE_NAME=mydatabase
3. Start the Services

   -Once everything is setup , start the services using Docker compose :
   docker-compose up -d
   Command will pull the necessary images, build the backed and start all the services in detached mode
4. Access the Application
   -- The frontend will be available at http://localhost:80.
   -- The backend and database services will communicate internally via the defined networks.
5. Additional Information

   -- Security: The database password is securely managed using Docker secrets.
   -- Resource Management: The backend service has CPU and memory limits to ensure efficient resource usage.
   -- Data Persistence: PostgreSQL data is stored in a volume, ensuring it remains intact even if the container restarts.
6. Contributing

   --If you'd like to contribute, please feel free to open an issue or submit a pull request. Any improvements or suggestions are welcome!
7. License
   -- Project is under Broadridge License  ##just added to make this last part of readme file

#################################### Python task #########################################################

-- First task
        -- Find the Maximum number of commits were made on dates and Minimum numbers of commits were made on dates (task.py).
-- Second task 
          -- The program is written to visualize the data in graph what the data is (analyze.py).

 ## Instructions to run the programs 
 
Task1 :
     -- Open the file path where the files are :
     -- Go to the path \broadridge-assessment\python-task.
     -- Then python task.py output will get displayed.
Task2 :
      -- Open the file path where the files are :
      -- Go to the path \broadridge-assessment\python-task.
      -- Then python analyze.py output will get displayed.