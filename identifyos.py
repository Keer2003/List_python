try:
    import platform
    import os
    osidentifier=platform.platform()
    print(osidentifier)
    if "Windows" in osidentifier:
        print("underlying os is window")
    elif "drawn" in osidentifier or "sonam" in osidentifier:
        print("underlying os is mac")
    else:
        print("underlying os is linx")
except Exception as e:
    print(e)

