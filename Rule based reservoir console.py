def reservoir_evaluation(gr, res, nphi, rhob):
    """gr   : Gamma Ray log (API)
    res  : Resistivity log (ohm.m)
    nphi : Neutron porosity log (v/v)
    rhob : Bulk density log (g/cc)
    """
    # 1. Lithology interpretation ---
    if 0 <= gr < 50:
        lithology = "Clean Sandstone"
    elif 50 <= gr < 100:
        lithology = "Shaly Sand"
    elif 100 <= gr <= 150:
        lithology = "Shale"
    else:
        lithology = "Outside defined range"

    # 2. Hydrocarbon zone interpretation ---
    if gr < 75 and res > 50:
        hc_zone = "Possible Hydrocarbon Zone"
    elif gr < 75 and res <= 50:
        hc_zone = "Likely Water-Bearing Zone"
    else:
        hc_zone = "Poor Reservoir / Shale Zone"

    # 3. Fluid type interpretation ---
    if res > 50 and nphi < 0.15 and rhob < 2.3:
        fluid = "Possible Gas"
    elif res > 50 and nphi >= 0.15:
        fluid = "Possible Oil"
    elif res <= 45:
        fluid = "Likely Water"
    else:
        fluid = "Uncertain"

    return {
        "lithology": lithology,
        "hydrocarbon_zone": hc_zone,
        "fluid_type": fluid,
    }


def get_float(prompt, low=None, high=None):
    """Prompt until the user enters a valid float, optionally within [low, high]."""
    while True:
        raw = input(prompt).strip()
        try:
            value = float(raw)
        except ValueError:
            print("  Please enter a valid number.")
            continue
        if low is not None and value < low:
            print(f"  Value must be >= {low}.")
            continue
        if high is not None and value > high:
            print(f"  Value must be <= {high}.")
            continue
        return value


def print_result(gr, res, nphi, rhob, result):
    print("\n--- Reservoir Evaluation Result ---")
    print(f"  GR   = {gr} API")
    print(f"  RES  = {res} ohm.m")
    print(f"  NPHI = {nphi} v/v")
    print(f"  RHOB = {rhob} g/cc")
    print("  -----------------------------")
    print(f"  Lithology        : {result['lithology']}")
    print(f"  Hydrocarbon Zone : {result['hydrocarbon_zone']}")
    print(f"  Fluid Type       : {result['fluid_type']}")
    print("------------------------------------\n")


def main():
    print("=== Reservoir Evaluation Console ===")
    print("Enter well log values to evaluate lithology, hydrocarbon zone, and fluid type.")
    print("Type 'q' at any prompt to quit.\n")

    while True:
        gr_raw = input("Gamma Ray (GR, API) [or 'q' to quit]: ").strip()
        if gr_raw.lower() == "q":
            break
        try:
            gr = float(gr_raw)
        except ValueError:
            print("  Please enter a valid number.\n")
            continue

        res = get_float("Resistivity (RES, ohm.m): ", low=0)
        nphi = get_float("Neutron Porosity (NPHI, v/v): ")
        rhob = get_float("Bulk Density (RHOB, g/cc): ")

        result = reservoir_evaluation(gr, res, nphi, rhob)
        print_result(gr, res, nphi, rhob, result)

        again = input("Evaluate another set of logs? (y/n): ").strip().lower()
        if again != "y":
            break

    print("Goodbye!")


if __name__ == "__main__":
    main()