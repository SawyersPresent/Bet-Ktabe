


- University management
	- It has a string `basePath` that has my set base path for all the files
		- Of course each file has its own file
	- Main menu is present with switch cases to give options




```java
import java.util.*;  
  
public class UniversityManagement {  
    private DepartmentManagerInterface departmentManager;  
    private EmployeeManager employeeManager;  
    private StudentCounselingManager studentCounselingManager;  
    private StudentPerformanceManagerInterface studentPerformanceManager;  
  
    public UniversityManagement() {  
        String basePath = "C:\\Users\\saif\\Desktop\\MAINHQ\\School\\advanced programming\\data set\\";  
        String departmentFilePath = basePath + "Department_Information.txt";  
        String employeeFilePath = basePath + "Employee_Information.txt";  
        String studentCounselingFilePath = basePath + "Student_Counceling_Information.txt";  
        String studentPerformanceFilePath = basePath + "Student_Performance_Data.txt";  
  
        this.departmentManager = new DepartmentManager(departmentFilePath);  
        this.employeeManager = new EmployeeManager(employeeFilePath);  
        this.studentCounselingManager = new StudentCounselingManager(studentCounselingFilePath);  
        this.studentPerformanceManager = new StudentPerformanceManager(studentPerformanceFilePath);  
    }  
  
    public static void main(String[] args) {  
        Scanner scanner = new Scanner(System.in);  
        UniversityManagement um = new UniversityManagement();  
  
        while (true) {  
            System.out.println("\nMain Menu:");  
            System.out.println("1. Retrieve Department by ID");  
            System.out.println("2. Retrieve Employee by ID");  
            System.out.println("3. Retrieve Student Counseling by ID");  
            System.out.println("4. Retrieve Student Performance by ID");  
            System.out.println("5. Retrieve Students by Department and DOB Range");  
            System.out.println("6. Retrieve Students by Department and DOA Range");  
            System.out.println("7. Get Student Performance Stats");  
            System.out.println("8. Get Department Stats");  
            System.out.println("9. Get Department Details");  
            System.out.println("10. Exit");  
            System.out.print("Choose an option: ");  
  
            int choice = scanner.nextInt();  
            scanner.nextLine(); // Consume newline  
  
            switch (choice) {  
                case 1:  
                    System.out.print("Enter Department ID: ");  
                    String deptId = scanner.nextLine();  
                    Department dept = um.departmentManager.getDepartmentByID(deptId);  
                    System.out.println(dept);  
                    break;  
                case 2:  
                    System.out.print("Enter Employee ID: ");  
                    String empId = scanner.nextLine();  
                    Employee emp = um.employeeManager.getEmployeeByID(empId);  
                    System.out.println(emp);  
                    break;  
                case 3:  
                    System.out.print("Enter Student Counseling ID: ");  
                    String scId = scanner.nextLine();  
                    StudentCounseling sc = um.studentCounselingManager.getStudentCounselingByID(scId);  
                    System.out.println(sc);  
                    break;  
                case 4:  
                    System.out.print("Enter Student Performance ID: ");  
                    String spId = scanner.nextLine();  
                    List<StudentPerformance> spList = um.studentPerformanceManager.getStudentPerformanceByID(spId);  
                    for (StudentPerformance sp : spList) {  
                        System.out.println(sp);  
                    }  
                    break;  
                case 5:  
                    System.out.print("Enter Department ID: ");  
                    String departmentIdDOB = scanner.nextLine();  
                    System.out.print("Enter Date of Birth Start (YYYY-MM-DD): ");  
                    String dobStart = scanner.nextLine();  
                    System.out.print("Enter Date of Birth End (YYYY-MM-DD): ");  
                    String dobEnd = scanner.nextLine();  
                    List<StudentCounseling> studentsByDOB = um.studentCounselingManager.getStudentsByDepartmentAndDOBRange(departmentIdDOB, dobStart, dobEnd);  
                    for (StudentCounseling student : studentsByDOB) {  
                        System.out.println(student);  
                    }  
                    break;  
                case 6:  
                    System.out.print("Enter Department ID: ");  
                    String departmentIdDOA = scanner.nextLine();  
                    System.out.print("Enter Date of Admission Start (YYYY-MM-DD): ");  
                    String doaStart = scanner.nextLine();  
                    System.out.print("Enter Date of Admission End (YYYY-MM-DD): ");  
                    String doaEnd = scanner.nextLine();  
                    List<StudentCounseling> studentsByDOA = um.studentCounselingManager.getStudentsByDepartmentAndDOARange(departmentIdDOA, doaStart, doaEnd);  
                    for (StudentCounseling student : studentsByDOA) {  
                        System.out.println(student);  
                    }  
                    break;  
                case 7:  
                    System.out.print("Enter Student ID: ");  
                    String studentId = scanner.nextLine();  
                    Map<String, Double> performanceStats = um.studentPerformanceManager.getStudentPerformanceStats(studentId);  
                    for (Map.Entry<String, Double> entry : performanceStats.entrySet()) {  
                        System.out.println(entry.getKey() + ": " + entry.getValue());  
                    }  
                    break;  
                case 8:  
                    System.out.print("Enter Department ID: ");  
                    String depId = scanner.nextLine();  
                    long employeeCount = um.departmentManager.getNumberOfEmployees(um.employeeManager.getEmployees(), depId);  
                    long studentCount = um.departmentManager.getNumberOfStudents(um.studentCounselingManager.getStudentCounselings(), depId);  
                    System.out.println("Number of Employees: " + employeeCount);  
                    System.out.println("Number of Students: " + studentCount);  
                    break;  
                case 9:  
                    System.out.print("Enter Department ID: ");  
                    String deptDetailId = scanner.nextLine();  
                    List<StudentCounseling> students = um.studentCounselingManager.getStudentsByDepartmentAndDOARange(deptDetailId, "0000-01-01", "9999-12-31");  
                    List<Employee> employees = um.employeeManager.getEmployees();  
                    System.out.println("Students:");  
                    for (StudentCounseling student : students) {  
                        System.out.println(student);  
                    }  
                    System.out.println("Employees:");  
                    for (Employee employee : employees) {  
                        if (employee.getDepartmentID().equals(deptDetailId)) {  
                            System.out.println(employee);  
                        }  
                    }  
                    break;  
                case 10:  
                    System.out.println("Exiting...");  
                    scanner.close();  
                    return;  
                default:  
                    System.out.println("Invalid choice. Please try again.");  
            }  
        }  
    }  
}
```