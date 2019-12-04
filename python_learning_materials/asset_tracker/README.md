# Asset Tracker Lab

## Goal
Demonstrate best practices of writing code TDD that interacts with external systems (WS, Email, etc.).

## Task
Create cronjob that will send an email with information about all the devices on a network.

Cronjob looks like this:

    0 0 * * * * /usr/bin/python /opt/asset_tracker/asset_tracker.py


## REST Endpoints

#### Retrieval of connected devices
URL: localhost:8080/connectedDevices

Method: GET

Sample payload:
    
    {
    	"subnets": [
    		{
    			"name": "HR Office",
	    		"subnet": "192.168.0.0/24",
		    	"devices": [
			    	{
			    		"owner": "matt.todd@asynchrony.com",
			    		"MAC": "20:c9:d1:37:bc:a5",
			    		"IPv4": "192.168.0.32",
			    		"joined_at": "2016-09-13 13:57:22",
			    		"lease_end": "2017-9-19",
			    		"lease_status": "active"
			    	},
			    	{
			    		"owner": "josh.duncan@asynchrony.com",
			    		"MAC": "53:d8:d1:c7:b8:a6",
			    		"IPv4": "192.168.0.22",
			    		"joined_at": "2016-09-12 10:33:02",
			    		"lease_end": "2019-11-30",
			    		"lease_status": "active"
			    	},
			    	...
		    	]
	    	}
    	]
    }

#### marking a device expired
URL: localhost:8080/setLease

Method: POST

Sample payload: 
```
{
	"MAC": "53:d8:d1:c7:b8:a6",
	"lease_status": "expired"
}
```

## Expected output

Report should include a list of all network devices

Sample email:
    
    Device Report For 9/14/2017
    
    SUBNET NAME: HR Office
    MASK: 192.168.0.0/24
    
    | IPv4         | MAC               | CONTACT                    | LEASE STATUS |
    --------------------------------------------------------------------------------
    | 192.168.0.32 | 20:c9:d1:37:bc:a5 | matt.todd@asynchrony.com   | Active       |
    | 192.168.0.22 | 53:d8:d1:c7:b8:a6 | josh.duncan@asynchrony.com | Expired      |


## Existing files

There already are some files with existing functionality that you will use to build your system.

### email_client.py

This will send out emails given plain text content. (Really it will just print your report on the screen so you can see your output)

To use: 

    EmailClient().send_email("foo@bar.com", "Important Message", "Hello world!")

### network\_devices\_client.py

To Be Implemented    
Should have two functions to access the specified endpoints and return the retrieved json data as objects

### report_generator.py

To Be Implemented    
Should parse data into a report and send it to a designated e-mail

### asset_updater.py

To Be Implemented    
Should accept the device list data    
Should use the specified endpoint to update devices that have expired but are not marked as such    
Should log any changes made to a file    
Should return the modified data to be used by report_generator    

### asset_tracker.py

Entry point for cron job.    
Should make use of the network\_devices\_client, report\_generator, and asset\_updater to "send a report", and log changes

## Dependencies

Run the following command

    $ pip install -U pytest

## To run the tests

    $ pytest
    
## To run the app locally

You will need to set the PYTHONPATH environment variable to the local directory (*asset_tracker*) to enable python to load your module.

    $ PYTHONPATH=$(pwd) python ./lib/asset_tracker.py

If you run this without any changes, you should see:

    Printing!





