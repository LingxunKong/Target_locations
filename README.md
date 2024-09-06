Method 1:
Direct web scrapping from Target.com

Method 2:
OpenStreetMap API
https://overpass-turbo.eu/#

[out:json][timeout:25];
area[name="United States"]->.searchArea;
node["shop"="department_store"]["name"="Target"](area.searchArea);
out body;
>;
out skel qt;


