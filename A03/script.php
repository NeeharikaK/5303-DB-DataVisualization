<?php
/**
 * This is an example php script that will:
 * 
 * 1: Connect to a mysql database on the local machine (cs2 server)
 * 2: Create a table called users (typically I would do that with phpMyAdmin)
 * 3: Add a primary key to the table (again phpMyadmin would be better)
 * 4: Opens a json formatted file, and loads it into the users table
 * 
 * You need to fill in the username, password, and database to make this 
 * script work for you.
 * 
 */
// Turn errors off later make the -1 a 0
error_reporting(-1);
// Fill in your connection info
$host = "localhost";
$username = "kasarla";
$password = 'ab0V7yqPzoJL';
$database = "kasarla";
// Do the connection
$conn = mysqli_connect($host, $username, $password, $database);
if (mysqli_connect_errno()) {
    echo "Failed to connect to MySQL: " . mysqli_connect_error();
}else{
    echo "Connected...\n";
}
// Drop a Table 
///////////////////////////////////////////////////////////////
// I did the drop because I ran this script multiple times and 
// wanted a clean slate every time. You can remove this
// if you want
//$sql = "DROP TABLE `users`;";
//$conn->query($sql);
// Create a Table
///////////////////////////////////////////////////////////////
// create your sql statement
//$sql = "CREATE TABLE `users` ( 
//    `id` int(11) NOT NULL, 
//    `first_name` varchar(32) NOT NULL, 
//    `last_name` varchar(32) NOT NULL, 
//    `email` varchar(127) NOT NULL, 
//    `gender` varchar(7) NOT NULL, 
//    `ip_address` varchar(15) NOT NULL 
//    );";

$sql = "CREATE TABLE `A04_routes` ( 
    `Airline` varchar(5) NOT NULL, 
    `Airline_ID` varchar(32) NOT NULL, 
    `Source_AP` varchar(32) NOT NULL, 
    `Source_AP_ID` varchar(127) NOT NULL, 
    `Dest_AP` varchar(7) NOT NULL, 
    `Dest_AP_ID` varchar(15) NOT NULL,
    `CodeShare` varchar(10) NOT NULL,
    `Stops` int(10) NOT NULL,
    `Equipment` varchar(3) NOT NULL 
    );";
// run your sql statement
$result = $conn->query($sql);
// if it was successful lets alter the table and add a key
if($result){
    $sql = "ALTER TABLE `A04_routes` ADD PRIMARY KEY (`Airline_ID`);";
    $conn->query($sql);
}
// Add data to Table
///////////////////////////////////////////////////////////////
// opens and reads entire file in one line
$data = file_get_contents('routes.json');
// turns json string into a php associative array 
$data = json_decode($data,true);
// loops through the array putting one user in $u at every iteration
foreach($data as $u){
    // some names have apostrophes so we need to
    // escape those or query qill fail
    // $fname = addslashes($u['first_name']);
    // $lname = addslashes($u['last_name']);
    // Build the insert statement pulling out the values from $u
    $sql = "INSERT INTO A04_routes VALUES ('{$u['Airline']}','{$u['Airline_ID']}','{$u['Source_AP']}',
                                    '{$u['Source_AP_ID']}','{$u['Dest_AP']}','{$u['Dest_AP_ID']}','{$u['CodeShare']}',
					'{$u['Stops']}','{$u['Equipment']}');";
    print($sql)."\n";
    $result = $conn->query($sql);
    if(!$result){
        echo "Error message: ". $conn->error;
    }
}