from extras.plugins import PluginConfig

class MacScannerConfig(PluginConfig):
    name = 'netbox-mac-scan',
    verbose_name = 'Mac Scanner',
    decription = 'A Netbox plugin for MAC address scanning',
    version = '0.1',
    author = 'Sean Collins',
    author_email = 'collsean@umich.edu',
    base_url = 'mac-scan',
    required_settings = []

config = MacScannerConfig