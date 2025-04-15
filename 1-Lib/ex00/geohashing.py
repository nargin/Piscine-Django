import sys
# import antigravity # could be useful for the future

def geohashing(lat: float, lon: float, precision: int = 5) -> str:
    """
    Convert latitude and longitude to a geohash string.
    Args:
        lat: Latitude (-90 to 90)
        lon: Longitude (-180 to 180)
        precision: Length of the geohash string (default 5)
    Returns:
        Geohash string
    """
    if lat < -90 or lat > 90 or lon < -180 or lon > 180:
        raise ValueError("Invalid latitude or longitude")

    base32 = '0123456789bcdefghjkmnpqrstuvwxyz'

    # Step 3: Initialize the boundaries for lat/lon
    lat_range = (-90.0, 90.0)
    lon_range = (-180.0, 180.0)

    # Step 4: Initialize variables to store binary encoding
    bits = []
    is_even = True  # Used to alternate between longitude and latitude

    # Step 5: Main encoding loop
    # We need 5 bits per character, so multiply precision by 5
    while len(bits) < precision * 5:
        if is_even:
            # Handle longitude
            mid = (lon_range[0] + lon_range[1]) / 2
            if lon < mid:
                bits.append(0)
                lon_range = (lon_range[0], mid)
            else:
                bits.append(1)
                lon_range = (mid, lon_range[1])
        else:
            # Handle latitude
            mid = (lat_range[0] + lat_range[1]) / 2
            if lat < mid:
                bits.append(0)
                lat_range = (lat_range[0], mid)
            else:
                bits.append(1)
                lat_range = (mid, lat_range[1])
        
        is_even = not is_even

    hash_str = ''
    for i in range(0, len(bits), 5):
        # Take 5 bits at a time and convert to base32
        chunk = bits[i:i+5]
        digit = sum(bit << (4-j) for j, bit in enumerate(chunk))
        hash_str += base32[digit]

    return hash_str

# Example usage
if __name__ == "__main__":
    result = geohashing(37.572381100574944, 126.98648665587018, 7)
    print(f"Geohash for (37.572381100574944, 126.98648665587018): {result}")