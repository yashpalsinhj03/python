
<%@ page import="java.sql.*" %>
<%
String url = "jdbc:mysql://localhost:3306/jspcurd";
String dbUser = "root";
String dbPass = "";

String message = "";
String action = request.getParameter("action");

if ("save".equals(action)) {
    String id = request.getParameter("id");
    String name = request.getParameter("name");
    String course = request.getParameter("course");
    String semester = request.getParameter("semester");

    try {
        Class.forName("com.mysql.cj.jdbc.Driver");

        try (Connection con =
                DriverManager.getConnection(url, dbUser, dbPass)) {

            if (id == null || id.trim().isEmpty()) {
                try (PreparedStatement ps = con.prepareStatement(
                    "INSERT INTO student(name, course, semester) VALUES(?,?,?)")) {
                    ps.setString(1, name);
                    ps.setString(2, course);
                    ps.setString(3, semester);
                    ps.executeUpdate();
                }
                message = "Student inserted successfully!";
            } else {
                try (PreparedStatement ps = con.prepareStatement(
                    "UPDATE student SET name=?, course=?, semester=? WHERE id=?")) {
                    ps.setString(1, name);
                    ps.setString(2, course);
                    ps.setString(3, semester);
                    ps.setInt(4, Integer.parseInt(id));
                    int rows = ps.executeUpdate();

                    message = rows > 0
                        ? "Student updated successfully!"
                        : "Student ID not found!";
                }
            }
        }
    } catch (Exception e) {
        message = "Error: " + e.getMessage();
    }
}
%>

<!DOCTYPE html>
<html>
<head>
    <title>Student Insert and Update</title>
</head>
<body>

<h2>Student Management</h2>

<p><%= message %></p>

<form method="post" action="index.jsp">
    <input type="hidden" name="action" value="save">

    ID (blank for Insert):
    <input type="number" name="id" min="1">
    <br><br>

    Name:
    <input type="text" name="name" required>
    <br><br>

    Course:
    <input type="text" name="course" required>
    <br><br>

    Semester:
    <input type="text" name="semester" required>
    <br><br>

    <button type="submit">Save</button>
</form>

</body>
</html>
