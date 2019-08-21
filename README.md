# Parametric-Curves-to-PLY
This is my code to generate parametric curves into ply files (which later can be converted to .stl).

In order to use: 

1. Define your parametric function in parametric_to_ply.py
2. In export_ply.py in main()
    a. define your pointcloud as a function by calling your parametric function
    b. call export_edges($NAMEOFPOINTCLOUDFUNCTION, 'name-of-export-file-you-want.ply')
    
My examples are still in there commented out for guidance. 
