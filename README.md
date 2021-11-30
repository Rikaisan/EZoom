# EZoom - The Automatic Zoom Client

EZoom is a Python application that lets you automate joining your meetings, it helps you join the specified meeting in the config with the press of a button!

All you have to do is configure your schedule and then run the python script!  
If successful, the zoom app will launch and automatically join the meeting scheduled for that time interval.  
If no meeting is defined, an error will appear:  
![Error Preview](https://i.imgur.com/gVdBKrV.png)

## Features

-   [x] Automatically define Zoom path
-   [x] Support for offsets
-   [x] Support for password meetings
-   [ ] Tool for generating schedules  

## Setup

**This project requires Python 3.9 or later to be installed**

1. Clone repository or download as zip and extract it
2. Define schedule in `schedule.json`
3. Configure offsets in `config.json`
4. Defining username **(Only if using a version lower than 3.0)**  
   The default Zoom installation directory is under

    > `"C:/Users/USERNAME/AppData/Roaming/Zoom/bin/Zoom.exe"`

    - Go to EZoom's `config.json` file and change the `USERNAME` field to match yours.
    - Set `use_custom_path` to `true`
    - In case you use another letter for your System Disk or use a custom installation path, specify it in the config file.

## Configuration

Offsets are used to offset the time the script allows you to enter a class, they are primarily used when you want to join a class early or disable joining in the last `X` minutes.  
Offsets are specified in minutes, `'start'` offsets the starting hour and `'end'` offsets the ending hour.

-   `{"start": 10}` means the starting hour will be offset by `00:10`:

    | Hour in schedule | Hour the program reads |
    | ---------------- | ---------------------- |
    | 08:30            | 08:40                  |
    | 18:50            | 19:00                  |

You can also specify negative numbers to be able to enter a meeting `X` minutes before the specified hour:

-   `{"start": -5}` means the starting hour will be offset by `-00:05`:

    | Hour in schedule | Hour the program reads |
    | ---------------- | ---------------------- |
    | 14:30            | 14:25                  |
    | 09:00            | 08:55                  |

If you set more than `60` minutes, the program will automatically change the correct amount of hours:

-   `{"end": -65}` means the ending hour will be offset by `-01:05`:

    | Hour in schedule | Hour the program reads |
    | ---------------- | ---------------------- |
    | 14:30            | 13:25                  |
    | 09:00            | 07:55                  |

## Setting up your Schedule

The schedule is setup so that you only need to add the days that you have meetings, meaning that if you only have meetings on Fridays and Sundays, you would have something like this:

```
{
	"Friday": {
		// Meetings
	},
	"Sunday": {
		// Meetings
	}
}
```

The convention is the following:

-   Day names must start with a capital letter and have lowercase letters for the rest of the string: `"Monday"`, `"Wednesday"`
-   Meeting times should use the following format: "Starting time - Ending time" -> `"11:00 - 14:00"`
-   Starting time must be a smaller number than the ending time
-   The number to connect to the meeting is the number found in meeting invite links:
    | Meeting link | Meeting ID |
    | ------------ | ---------- |
    | https://zoom.us/j/29694775121 | 29694775121 |

A valid schedule would look something like this:

```
{
	"Tuesday": {
		"09:15 - 11:15": 99955645115,
		"12:00 - 14:00": 29694775121
	},
	"Thursday": {
		"18:30 - 20:00": 91344875615
	},
	"Friday": {
		"18:30 - 20:00": 29694775121
	}
}
```

## Meetings with password

You can also join meetings that require a password to join, just get the invite link with the password included and use a list instead of an integer:  
`[4649434460, "Wk9udnprWFNkNjJRcmp5RDZUeHVWUT09"]`

> Link: `https://zoom.us/j/5519459264?pwd=Wk9udnprWFNkNjJRcmp5RDZUeHVWUT09`  
> ID: `5519459264` PWD: `Wk9udnprWFNkNjJRcmp5RDZUeHVWUT09`

To get this link, while in a meeting, click the arrow on the members button and choose invite, then click **Copy Invite Link**.

-   Having the ID inside a set of [] with no password is also valid: `[1681607159]`
-   Example Schedule with meetings that require password:

    ```
    {
    	"Monday": {
    		"10:00 - 12:00": [4649434460, "QUVLNkpCMm53bkNjYlFNYVZUK1NWZz09"],
    		"13:00 - 16:00": 1681607159
    	},
    	"Tuesday": {
    		"07:00 - 09:00": 7875122923,
    		"10:30 - 12:00": [4649434460, "Wk9udnprWFNkNjJRcmp5RDZUeHVWUT09"],
    		"13:00 - 15:00": 1681607159
    	},
    	"Wednesday": {
    		"14:00 - 16:00": 7875122923
    	},
    	"Thursday": {
    		"09:00 - 10:00": [4649434460, "QUVLNkpCMm53bkNjYlFNYVZUK1NWZz09"],
    		"10:00 - 12:00": 4649434460,
    		"16:00 - 18:00": 7875122923
    	},
    	"Friday": {
    		"07:00 - 10:00": [4649434460, "QUVLNkpCMm53bkNjYlFNYVZUK1NWZz09"],
    		"10:30 - 12:00": 5519459264,
    		"13:00 - 15:00": [4649434460, "Wk9udnprWFNkNjJRcmp5RDZUeHVWUT09"]
    	},
    	"Saturday": {
    		"07:30 - 09:00": 5519459264,
    		"11:00 - 13:00": 4649434460
    	}
    }
    ```

---

Feel free to send suggestions and feedback to feedback@rikaisan.com!
