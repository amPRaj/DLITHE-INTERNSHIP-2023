<?php

    include_once('db.php');

    echo "<h1>Welcome</h1>";

    $name=$_REQUEST['name'];

    $sql="select * from attendance where name='$name' and cdt=current_date()";
    
    $res=execute( $sql );
    $row=$res->fetch_object();

    if(isset($row))
    {

        return;
    }


    $sql="insert into attendance(name,cdt) values('$name',current_date())";

    execute($sql);
    
    echo "Ok saved";
   

?>