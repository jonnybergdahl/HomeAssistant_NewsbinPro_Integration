# Newsbin Pro integration for Home Assistant

This is an integration to control Newsbin Pro from within Home Assistant. 


## Installation

### Setup Newsbin Pro

In Newsbin Pro, select the menu _Options_ - _Settings_. In the left pane select _Remote Control_.

![settings.png](https://raw.githubusercontent.com/jonnybergdahl/HomeAssistant_NewsbinPro_Integration/main/images/settings.png)

Check the _Enable Remote Control_ checkbox and enter a password in the _Password_ field. 
Then click _OK_.

### Install integration

Click the button to add this repository to HACS.

[![Open your Home Assistant instance and open a repository inside the Home Assistant Community Store.](https://my.home-assistant.io/badges/hacs_repository.svg)](https://my.home-assistant.io/redirect/hacs_repository/?owner=jonnybergdahl&category=Integration&repository=HomeAssistant_NewsbinPro_Integration)

Then restart Home Assistant.

You can also do the above manually:
1. Open the Home Assistant web interface and navigate to the HACS store.
2. Click on the "Integrations" tab.
3. Click on the three dots in the top right corner and select "Custom repositories".
4. Enter the URL (`https://github.com/jonnybergdahl/HomeAssistant_NewsbinPro_Integration`) and select "Integration" as the category.
5. Click "Add".
6. Once the repository has been added, you should see the Elecrow GrowCube integration listed in the HACS store.
7. Click on the integration and then click "Install".
8. Restart Home Assistant.

## Add a Newsbin Pro device

Click the button to add a Growcube device to Home Assistant.

[![Open your Home Assistant instance and start setting up a new integration.](https://my.home-assistant.io/badges/config_flow_start.svg)](https://my.home-assistant.io/redirect/config_flow_start/?domain=newsbinpro)

Click OK when it asks if you want to setup the Newsbin Pro integration.

![wizard1.png](https://raw.githubusercontent.com/jonnybergdahl/HomeAssistant_NewsbinPro_Integration/main/images/wizard1.png)

Enter the IP address, port and password for the Newsbin Pro instance and click Submit.

![wizard2.png](https://raw.githubusercontent.com/jonnybergdahl/HomeAssistant_NewsbinPro_Integration/main/images/wizard2.png)

You can also do this manually:

1. Open the Home Assistant web interface.
2. Click on "Configuration" in the left-hand menu.
3. Click on "Integrations".
4. Click on the "+" button in the bottom right corner.
5. Search for "Newsbin" and click on it.
6. Enter the IP address (or host name), port and password of the device.

And that's it! You should now be able to see its status and control it from the Home Assistant web interface.

## Getting help

You can file bugs in the [issues section on Github](https://github.com/jonnybergdahl/HomeAssistant_NewsbinPro_Integration/issues).

You can also reach me at [#jonnys-place](https://discord.gg/SeHKWPu9Cw) on Brian Lough's Discord.
