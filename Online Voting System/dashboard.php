<?php
    /*session_start();

    if(!isset($_SESSION['userdata'])){
        header("location: index.html");
    }*/

    /*$userdata = $_SESSION['userdata'];*/
?>


<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>OVS - Dashboard</title>
    <link rel="stylesheet" href="style.css">
</head>
<body>
    <style>
        #backbtn{
            padding: 15px;
            border-radius: 8px;
            background-color: rgb(0,0,83);
            color: white;
            text-transform: uppercase;
            width: 100px;
            float: left;
        }

        #logoutbtn{
            padding: 15px;
            border-radius: 8px;
            background-color: rgb(0,0,83);
            color: white;
            text-transform: uppercase;
            width: 100px;
            float: right;
        }
    </style>
    <div id="mainSection">
        <div id="headerSection">
            <button id="backbtn">Back</button>
            <button id="logoutbtn">Log Out</button>
            <img src="OVS_logo.jpg" alt="OVS logo" class="center">
            <h1>Online Voting System</h1>
        </div>

        <hr>

        <div id="Profile">
        </div>
        <div id="Group">

        </div>

    </div>
</body>
</html>