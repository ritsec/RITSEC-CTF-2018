<?php
include "header.php";
include "db.php";

// Check if POST
if (isset($_POST['username'])) {
    $result = $conn->query("SELECT * FROM test WHERE username='" . $_POST['username'] . "';");

    if(!$result) {
        echo "query failed!";
    } else {
        while($row = $result->fetch_assoc()) {
            echo "username: " . $row["username"] . " - passwd: " . $row["passwd"] . "<br>";
        }
    }

}
?>
<form action="/index.php" method="POST">
    Username: <br>
    <input type="text" name="username" placeholder="joe" /><br />
    <input type="submit" value="gogogo!" />
</form>

<?php include "footer.php" ?>