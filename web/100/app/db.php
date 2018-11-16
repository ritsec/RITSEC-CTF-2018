<?php
$servername = "database";
$username = "webserver";
$password = "password2";
$dbname = "challenge";

$conn = new mysqli($servername, $username, $password, $dbname);

if ($conn->connect_error) {
    die("connection failed: " . $conn->connect_error);
}