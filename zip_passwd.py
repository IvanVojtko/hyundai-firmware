import hashlib

def get_system_property(property_name):
    system_properties = {
        "ro.product.model": "daudioplus",
        "ro.product.brand": "hyundai",
        "ro.product.name": "pden_eu",
        "ro.product.device": "daudiopluslow_dab_pden_eu",
        "ro.product.board": "daudio",
        "ro.product.cpu.abi": "armeabi-v7a",
        "ro.product.cpu.abi2": "armeabi",
        "ro.product.manufacturer": "mobis",
        "ro.product.locale.language": "en",
        "ro.product.locale.region": "GB"
    }
    return system_properties.get(property_name, "")

def sha512_hash(value):
    return hashlib.sha512(value.encode()).hexdigest()

def get_password():
    temp_name2 = get_system_property("ro.product.name")
    temp_device2 = get_system_property("ro.product.device")

    tmp1 = (
        f"ro.product.model={get_system_property('ro.product.model')}"
        f"ro.product.brand={get_system_property('ro.product.brand')}"
        f"ro.product.name={temp_name2}"
        f"ro.product.device={temp_device2}"
        f"ro.product.board={get_system_property('ro.product.board')}"
        f"ro.product.cpu.abi={get_system_property('ro.product.cpu.abi')}"
        f"ro.product.cpu.abi2={get_system_property('ro.product.cpu.abi2')}"
        f"ro.product.manufacturer={get_system_property('ro.product.manufacturer')}"
        f"ro.product.locale.language={get_system_property('ro.product.locale.language')}"
        f"ro.product.locale.region={get_system_property('ro.product.locale.region')}"
    )

    re_val = sha512_hash(tmp1).upper()
    return sha512_hash(re_val).upper()[10:38]

print(get_password())

