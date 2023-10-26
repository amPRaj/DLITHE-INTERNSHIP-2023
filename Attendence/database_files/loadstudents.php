<?php

        include_once('db.php');
        $sql="select * from attendance ";
        
        $res=execute($sql);
        
        echo "<div class='container bg-info'>";
        echo "<table class='table' style=''>";
        echo "<tr><th>ID</th><th>Name</th><th>Date</th></tr>";

        while( $row=$res->fetch_object() )
        {

            echo "<tr>";

            echo "<td>$row->id</td>";
            echo "<td>$row->name</td>";
            echo "<td>$row->cdt</td>";
            

            echo "</tr>";
        }
        echo "</table>";

    ?>
  