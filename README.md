# Leave Management System

**How to run the Project:**
1. Clone this repo using 
   - `git clone https://github.com/DhivyaBharathi2923/leave_mangement_stystem`
2. Install IDE of your choice.
3. Use XAMPP or any server of your choice.
4. First create the MySql database using the mysql file in the repo
5. And then build and run the project from the IDE. 
**Login Information** <br>

user id :7<br>
name:DHIVYABHARATHI<br>
email:21ucav044@vicas.org<br>
 password: 123<br>
  note: The login information can be changed while setting up MySQL or via UI later
## Introduction
 Leave Management System (LMS) project with a Database Management System (DBMS) using Python and MySQL
In the dynamic landscape of modern workplaces, effective management of student leave has become a crucial aspect of organizational workflow. The Leave Management System (LMS) is a comprehensive solution designed to automate and streamline the leave request and approval process within an organization. Leveraging the power of a Database Management System (DBMS), this project aims to provide an efficient, secure, and user-friendly platform for students and managers to manage the leave life cycle seamlessly.


### Project Scope

The Leave Management System with DBMS is envisioned as a feature-rich platform catering to the diverse needs of both student and managers. The system facilitates the entire leave management process, from leave request submission to approval and record-keeping. It provides a centralized repository for all leave-related data, promoting data integrity, accessibility, and ease of reporting.

## Key Features

### 1. User Authentication and Authorization

The system ensures secure user authentication, allowing employees and managers to access only the functionalities relevant to their roles. Robust authorization mechanisms guarantee data privacy and prevent unauthorized access.

### 2. Leave Request Submission

student can submit leave requests through an intuitive and user-friendly interface. The system captures essential details such as the start date, end date, type of leave, and reason for leave.

### 3. Leave Approval Workflow

Managers are empowered with a streamlined interface to review and approve leave requests efficiently. Multi-level approval workflows can be configured to align with the organizational hierarchy.

### 4. Leave Balances and Entitlements

The system maintains accurate records of leave balances and entitlements for each student. Real-time updates ensure that both employees and managers have visibility into available leave quotas.


### 5. Leave History and Reporting

student can access their complete leave history, including approved, pending, and rejected leaves. Managers have the capability to generate reports for leave trends and analyze historical data.



## Project Objectives

1. **Efficiency:** Reduce the time and effort involved in the leave management process, enabling employees and managers to focus on their core responsibilities.

2. **Transparency:** Enhance transparency by providing real-time visibility into leave balances, approval workflows, and historical leave data.

3. **User Satisfaction:** Improve the overall employee experience by offering a user-friendly and intuitive platform for leave management.

4. **Data Security:** Implement robust security measures to safeguard sensitive employee data and ensure compliance with data protection regulations.

5. **Scalability:** Design the system to be scalable, accommodating the growth of the organization and evolving leave management requirements.

## Future Enhancements

The project's modular architecture allows for future enhancements and integrations, including but not limited to:
- notification
- Integration with head department systems for seamless data exchange.
- Advanced analytics for predictive leave management.
- Mobile applications for on-the-go leave requests and approvals.

## Conclusion

The Leave Management System with DBMS is poised to revolutionize how organizations handle leave management, bringing efficiency, transparency, and a modern user experience to this critical aspect of human resources management. This project strives to contribute to a healthier work-life balance for employees and a more streamlined process for managers, ultimately fostering a positive and productive work environment.
The Leave Management System is a Database Management System (DBMS) project designed to automate and streamline the leave request and approval process within an organization. It provides a centralized platform for employees to request leaves and for managers to efficiently manage and approve those requests.




## Technologies Used

- Frontend: HTML, CSS, JavaScript
- Backend: [python, Flask]
- Database: [ MySQL]





### Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/your-username/leave-management-system.git
   cd leave-management-system
   ```

2. [Additional steps if any, e.g., setting up the database]

3. Install dependencies:
   ```bash
   npm install  # or yarn install
   ```

## Usage

1. Start the application:
   ```bash
   npm start  # or yarn start
   ```

2. Open your web browser and navigate to http://127.0.0.1:5000

3. Log in with your credentials (use sample credentials if available).
Fig 1: ER Diagram
An Entity-Relationship (ER) model is a visual representation of the data model for a database system. For a Leave Management System (LMS) project, the ER model should capture the key entities, their attributes, and the relationships between them. Below is a simplified ER model for a basic LMS:



### Entities:

1. **User:**
   - Attributes: UserID (Primary Key), Username, Password, Role, Email, etc.

2. **LeaveRequest:**
   - Attributes: RequestID (Primary Key), UserID (Foreign Key), StartDate, EndDate, LeaveType, Reason, Status, Timestamp, etc.

3. **LeaveBalance:**
   - Attributes: UserID (Primary Key, Foreign Key), LeaveType, Entitlement, Balance, etc.

### Relationships:

1. **User - LeaveRequest (One-to-Many):**
   - One user can have multiple leave requests.
   - Each leave request is associated with one user.

2. **User - LeaveBalance (One-to-One):**
   - Each user has one leave balance for each leave type.
   - Each leave balance is associated with one user and one leave type.

### Cardinality:

- The relationship between User and LeaveRequest is one-to-many, indicating that one user can have multiple leave requests, but each leave request is associated with only one user.

- The relationship between User and LeaveBalance is one-to-one, indicating that each user has one leave balance entry for each leave type.

### Additional Considerations:

- The UserID in the User entity serves as a primary key and is referenced as a foreign key in the LeaveRequest and LeaveBalance entities to establish relationships.

- The Status attribute in the LeaveRequest entity represents the approval status of the leave request (e.g., Pending, Approved, Rejected).

This is a simplified ER model, and depending on the specific requirements and complexities of your LMS project, you may need to extend or modify the model. For instance, you might introduce additional entities such as Managers, Departments, or a more detailed LeaveType entity. Adjustments can be made based on the features and functionalities your LMS is intended to support.

# Chapter 3 - IMPLEMENTATION <br>
**Description on Implementation**<br>
The goal of this application is to manage the leave mangement our institution. <br><br>
**List of modules:**<br>
o	Login page<br>
o	Home page<br>
o	leave application<br>
o	leave satuts<br>
o	my leave<br>
o	leave approv<br>
o	leave reject<br>
o	admin login<br
o	pending request<br>
