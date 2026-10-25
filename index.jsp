
<%@ page import="java.sql.*" %>
<%
String url = "jdbc:mysql://localhost:3307/jspcurd";
String dbUser = "root";
String dbPass = "";

String action = request.getParameter("action");
String id = request.getParameter("id");
String name = request.getParameter("name");
String course = request.getParameter("course");
String semester = request.getParameter("semester");

String editId = "";
String editName = "";
String editCourse = "";
String editSemester = "";

try {
    Class.forName("com.mysql.cj.jdbc.Driver");

    try (Connection con = DriverManager.getConnection(url, dbUser, dbPass)) {

        if ("save".equals(action)) {
            if (id != null && !id.isEmpty()) {
                try (PreparedStatement ps = con.prepareStatement(
                    "UPDATE student SET name=?, course=?, semester=? WHERE id=?")) {
                    ps.setString(1, name);
                    ps.setString(2, course);
                    ps.setString(3, semester);
                    ps.setInt(4, Integer.parseInt(id));
                    ps.executeUpdate();
                }
            } else {
                try (PreparedStatement ps = con.prepareStatement(
                    "INSERT INTO student(name, course, semester) VALUES(?,?,?)")) {
                    ps.setString(1, name);
                    ps.setString(2, course);
                    ps.setString(3, semester);
                    ps.executeUpdate();
                }
            }

            response.sendRedirect("index.jsp");
            return;
        }

        if ("delete".equals(action) && id != null) {
            try (PreparedStatement ps = con.prepareStatement(
                "DELETE FROM student WHERE id=?")) {
                ps.setInt(1, Integer.parseInt(id));
                ps.executeUpdate();
            }

            response.sendRedirect("index.jsp");
            return;
        }

        if ("edit".equals(action) && id != null) {
            try (PreparedStatement ps = con.prepareStatement(
                "SELECT * FROM student WHERE id=?")) {
                ps.setInt(1, Integer.parseInt(id));

                try (ResultSet rs = ps.executeQuery()) {
                    if (rs.next()) {
                        editId = rs.getString("id");
                        editName = rs.getString("name");
                        editCourse = rs.getString("course");
                        editSemester = rs.getString("semester");
                    }
                }
            }
        }
%>
<!DOCTYPE html>
<html>
<head>
    <title>Student CRUD</title>
</head>
<body>

<h2>Student Management System</h2>

<h3><%= editId.isEmpty() ? "Add Student" : "Update Student" %></h3>

<form method="post" action="index.jsp">
    <input type="hidden" name="action" value="save">
    <input type="hidden" name="id" value="<%= editId %>">

    Name:
    <input type="text" name="name" value="<%= editName %>" required>
    <br><br>

    Course:
    <input type="text" name="course" value="<%= editCourse %>" required>
    <br><br>

    Semester:
    <input type="text" name="semester" value="<%= editSemester %>" required>
    <br><br>

    <button type="submit">Save</button>
    <a href="index.jsp">Clear</a>
</form>

<hr>
<h3>Student Records</h3>

<table border="1" cellpadding="8">
<tr>
    <th>ID</th>
    <th>Name</th>
    <th>Course</th>
    <th>Semester</th>
    <th>Action</th>
</tr>

<%
        try (Statement st = con.createStatement();
             ResultSet rs = st.executeQuery("SELECT * FROM student ORDER BY id")) {

            while (rs.next()) {
%>
<tr>
    <td><%= rs.getInt("id") %></td>
    <td><%= rs.getString("name") %></td>
    <td><%= rs.getString("course") %></td>
    <td><%= rs.getString("semester") %></td>
    <td>
        <a href="index.jsp?action=edit&id=<%= rs.getInt("id") %>">Edit</a>
        |
        <a href="index.jsp?action=delete&id=<%= rs.getInt("id") %>"
           onclick="return confirm('Delete this student?')">Delete</a>
    </td>
</tr>
<%
            }
        }
    }
} catch (Exception e) {
    out.println("<h3>Database Error</h3>");
    out.println("<pre>" + e.getMessage() + "</pre>");
}
%>
</table>

</body>
</html>
