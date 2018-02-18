sudo echo | gyc -E -Wp,-v - &> files
Y_INCLUDE_PATH=$(sudo grep -A1 "<...>" files | tail -n -1)/ymir/
sudo echo $Y_INCLUDE_PATH
sudo cp -r core/ $Y_INCLUDE_PATH
sudo cp -r std/ $Y_INCLUDE_PATH
sudo rm files

