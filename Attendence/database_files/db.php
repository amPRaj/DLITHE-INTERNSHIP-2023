<?php

    function execute( $sql )
    {
        $conn=mysqli_connect('localhost','root','','gmit');

        if( !$conn )
        {
            die(mysqli_connect_error());
        }

        $res=$conn->query( $sql);

        if( !$res )
        {
            die( mysqli_error($conn));
        }

        return $res;
    }


?>