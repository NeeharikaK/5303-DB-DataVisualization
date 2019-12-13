<?php

error_reporting(-1);

$conn = mysqli_connect('localhost', 'diekhoff', '', 'diekhoff');
if (mysqli_connect_errno()) {
    echo "Failed to connect to MySQL: " . mysqli_connect_error();
}else{
    echo "Connected...";
}

function visitEachCountry(){
	global $conn;
	
	$sql = "DROP TABLE `a06_visit_each_country`;";
	$conn->query($sql);
	
	$sql = "CREATE TABLE `a06_visit_each_country` 
	(`order` INT(11) NOT NULL, 
	`airport_id` INT(11) NOT NULL, 
	`name` VARCHAR (127) NOT NULL, 
	`country` VARCHAR (127) NOT NULL, 
	`city` VARCHAR (127) NOT NULL, 
	`longitude` VARCHAR (63) NULL, 
	`latitude` VARCHAR (63) NULL)";

	$conn->query($sql);

	$sql = "SELECT distinct(country) FROM `a06_airports` ";
	echo"<pre>";
	
	$result = $conn->query($sql);
	$airports = [];
	
	while($row = mysqli_fetch_assoc($result)){
		$sql1 = "SELECT * FROM `a06_airports` WHERE `country` = '{$row['country']}' 
		order by rand() LIMIT 1";
		
		$sub_result = $conn->query($sql1);
		$row2 = mysqli_fetch_assoc($sub_result);
		$airports[] = $row2;
	}
	
	$i = 0;
	foreach($airports as $airport){
		$a = $airport['airport_id'];
        $b = str_replace("'", '', $airport['name']);
        $c = $airport['country'];
        $d = str_replace("'", '', $airport['city']);
        $e = $airport['longitude'];
		$f = $airport['latitude'];
	
		$sql = "INSERT INTO `a06_visit_each_country` VALUES ('{$i}','{$a}','{$b}','{$c}','{$d}','{$e}','{$f}')";
		
		$res = $conn->query($sql);
		if(!$res){
			echo "\n\ntrouble with number {$i}\n\n {$b} \n";
			printf("Errormessage: %s\n", $conn->error);
		}
        $i++;
	}
}

visitEachCountry();