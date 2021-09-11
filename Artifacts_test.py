from Artifacts import Artifact

# dictionary for build_type and desirable stats
build_types_test = {"dps": [["critr", "critd"], ["atk%"]], "hp sup": [["hp%", "flathp"], ["er"]],
               "atk sup": [["atk%", "flatatk"], ["er"]], "anemo/em": [["em", "er"], ["atk%"]],
               "def": [["def%", "flatdef"], ["critr", "critd"]]}

test_artifact_1 = Artifact("Crimson Witch", ["critr", "flatatk", "em", "hp%"], "atk%", 7.0, "timepiece", 0)
test_artifact_2 = Artifact("Thundering Fury", ["critr", "critd", "atk%"], "flatatk", 47.0, "feather", 0)
test_artifact_3 = Artifact("Tenacity of the Millelith", ["hp%", "flathp", "flatatk"], "atk%", 7.0, "timepiece", 0)


print("test 1 potentials:", test_artifact_1.calculate_potential(build_types_test))
print("test 2 potentials:", test_artifact_1.calculate_potential(build_types_test))
print("test 3 potentials:", test_artifact_1.calculate_potential(build_types_test))
print("test 2 base value:", test_artifact_2.calculate_base_value("dps", build_types_test))

