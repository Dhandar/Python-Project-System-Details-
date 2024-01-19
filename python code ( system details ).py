# 1) All Installed software’s list
import psutil

# 2 ) Internet Speed
import speedtest

# 3 ) Screen resolvution
import socket

# 4) CPU model
import platform

# 5 ) No of core and threads of CPU
# It is completed in 4 

# 6) GPU model ( If exist )
import wmi

# 7 ) RAM Size ( In GB )

# 8 ) Screen size ( like, 15 inch, 21 inch)

# 9 ) Wifi/Ethernet mac address
import getmac

# 10 ) Public IP address




# 1) creating a function 
def get_installed_software():
    installed_software = []
    for app in psutil.process_iter(['pid', 'name']):
        installed_software.append(app.info['name'])
    return installed_software

# 2 ) 
def get_internet_speed():
    st = speedtest.Speedtest()
    download_speed = st.download()
    upload_speed = st.upload()
    return download_speed, upload_speed

# 3)
def get_system_resolution():
    try:
        from screeninfo import get_monitors
        monitors = get_monitors()
        resolutions = [(monitor.width, monitor.height) for monitor in monitors]
        return resolutions
    except ImportError:
        return "Screeninfo library not installed. Please install it using 'pip install screeninfo'."


# 4) 
def get_cpu_info():
    cpu_info = {}
    cpu_info['model'] = platform.processor()
    cpu_info['cores'] = psutil.cpu_count(logical=False)
    cpu_info['threads'] = psutil.cpu_count(logical=True)
    return cpu_info

# 5) Its a completed


# 6 ) 
def get_gpu_info():
    try:
        w = wmi.WMI()
        gpu_info = [gpu.Name for gpu in w.Win32_VideoController()]
        return gpu_info
    except Exception as e:
        return f"Error fetching GPU info: {e}"
    
# 7 )
def get_ram_size():
    ram_info = psutil.virtual_memory()
    return ram_info.total / (1024 ** 3)  # Convert to GB

# 8 ) 
def get_screen_size():
    try:
        from screeninfo import get_monitors
        monitors = get_monitors()
        screen_sizes = [f"{monitor.width}x{monitor.height} inch" for monitor in monitors]
        return screen_sizes
    except ImportError:
        return "Screeninfo library not installed. Please install it using 'pip install screeninfo'."
    
# 9 )
def get_network_info():
    mac_address = getmac.get_mac_address()
    hostname = socket.gethostname()
    ip_address = socket.gethostbyname(hostname)
    return mac_address, ip_address

# 10 ) 
def get_windows_version():
    return platform.version()



if __name__ == "__main__":
    installed_software = get_installed_software()
    download_speed, upload_speed = get_internet_speed()
    resolutions = get_system_resolution()
    cpu_info = get_cpu_info()
    gpu_info = get_gpu_info()
    ram_size = get_ram_size()
    screen_sizes = get_screen_size()
    mac_address, ip_address = get_network_info()
    windows_version = get_windows_version()



print("Installed Software:", installed_software)
print("Internet Speed (Download/Upload):-","Download Speed : " ,download_speed, "Mbps /", "Upload Speed : ",upload_speed, "Mbps")
print("Screen Resolutions:", resolutions)
print("CPU Model:", cpu_info['model'])
print("Number of Cores:", cpu_info['cores'])
print("GPU Model:", gpu_info if gpu_info else "No GPU detected")
print("RAM Size:", round(ram_size, 2), "GB")
print("Screen Sizes:", screen_sizes)
print("MAC Address:", mac_address)
print("IP Address:", ip_address)
print("Windows Version:", windows_version)

