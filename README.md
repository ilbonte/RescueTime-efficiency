RescueTime-efficiency
=====================

Discover which hours have been the most efficiency for you.

### What you need:
1.  [Python 3](https://www.python.org/)
2. [Matplotlib](http://matplotlib.org/)
3. [A RescueTime API key](https://www.rescuetime.com/anapi/manage)

###How to use the script
Open the .py file and in the first lines you will find:
```python
pv="interval"
rk = "efficiency" 
format = "csv" 
rs="hour" 
rb="2014-10-16" 
re="2014-11-16" 
rtapi_key="PUT_YOUR_API_KEY_HERE" 
file_name="file" 
```
You only need to change the last five parameters:

1. **rs** stand for "resolution_time" and it could be "hour" or "minute". I suggest to use "minute" only when you have few data (like a week)

2. **rb** stand for "restrict_begin" Sets the start day for data batch

3. **re** stand for "restrict_begin" Sets the end for data batch

4. **rtapi_key** is your API key

5. **file_name** is the name of the csv file that will be downloaded



```python
rs="hour" 
rb="2014-10-16" 
re="2014-11-16" 
rtapi_key="PUT_YOUR_API_KEY_HERE" 
file_name="file"  
```
For full documentation see: [A RescueTime API key](https://www.rescuetime.com/apidoc)

After finish the setup you can run the script.

Depending on your connection speed, computer performace and mostly the amount of data that you are going to plot it could take some seconds


###Examples 
Example of 1 month of data: I work better before 2pm
![alt text][one]

[one]: http://i62.tinypic.com/2z8xdv7.png


Example of 3 month of data: Of course if I have to stay up during the night I'm more motivated to work :|
![alt text][three]

[three]: http://i59.tinypic.com/24fbfv7.png
