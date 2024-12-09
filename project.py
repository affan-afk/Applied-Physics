# Name:Muhammad Affan Rasheed
# Student ID: 24K-0579
# Applied Physics Basic Vector Operations Project 2024



import numpy as np


def add_vectors(v1, v2):
    return np.add(v1, v2)


def subtract_vectors(v1, v2):
    return np.subtract(v1, v2)


def scalar_multiply(v, scalar):
    return np.multiply(v, scalar)


def dot_product(v1, v2):
    return np.dot(v1, v2)


def cross_product(v1, v2):
    return np.cross(v1, v2)


def magnitude(v):
    return np.linalg.norm(v)


def unit_vector(v):
    mag = magnitude(v)
    if mag == 0:
        return "Zero vector has no unit vector."
    return v / mag


def projection(v1, v2):
    scalar_proj = dot_product(v1, v2) / magnitude(v2)
    vector_proj = scalar_proj * (v2 / magnitude(v2))
    return scalar_proj, vector_proj


def angle_between(v1, v2):
    dot_prod = dot_product(v1, v2)
    magnitudes = magnitude(v1) * magnitude(v2)
    if magnitudes == 0:
        return 0
    cos_angle = dot_prod / magnitudes
    angle = np.arccos(np.clip(cos_angle, -1.0, 1.0))
    return np.degrees(angle)


def resultant(vectors):
    return np.sum(vectors, axis=0)


def triple_product(v1, v2, v3):
    scalar_triple = dot_product(cross_product(v1, v2), v3)
    vector_triple = np.cross(v1, np.cross(v2, v3))
    return scalar_triple, vector_triple


def rotate_vector(v, angle, axis="z"):
    angle = np.radians(angle)
    if axis == "z":
        rotation_matrix = np.array([[np.cos(angle), -np.sin(angle), 0],
                                    [np.sin(angle), np.cos(angle), 0],
                                    [0, 0, 1]])
    elif axis == "y":
        rotation_matrix = np.array([[np.cos(angle), 0, np.sin(angle)],
                                    [0, 1, 0],
                                    [-np.sin(angle), 0, np.cos(angle)]])
    elif axis == "x":
        rotation_matrix = np.array([[1, 0, 0],
                                    [0, np.cos(angle), -np.sin(angle)],
                                    [0, np.sin(angle), np.cos(angle)]])
    else:
        return "Invalid axis."
    return np.dot(rotation_matrix, v)


def main():
    print("=== Vector and Scalar Operations Program ===")
    operations = {
        1: "Add two vectors",
        2: "Subtract two vectors",
        3: "Multiply a vector by a scalar",
        4: "Dot product of two vectors",
        5: "Cross product of two vectors",
        6: "Magnitude of a vector",
        7: "Unit vector",
        8: "Projection of one vector onto another",
        9: "Angle between two vectors",
        10: "Resultant of multiple vectors",
        11: "Scalar and Vector Triple Product",
        12: "Rotate a vector",
        0: "Exit"
    }
    for key, val in operations.items():
        print(f"{key}. {val}")

    while True:
        choice = int(input("\nChoose an operation (0 to exit): "))
        if choice == 0:
            print("Exiting program. Goodbye!")
            break

        if choice in [1, 2, 4, 5, 9]:
            v1 = np.array(list(map(float, input("Enter first vector (comma-separated): ").split(','))))
            v2 = np.array(list(map(float, input("Enter second vector (comma-separated): ").split(','))))
            if choice == 1:
                print("Result:", add_vectors(v1, v2))
            elif choice == 2:
                print("Result:", subtract_vectors(v1, v2))
            elif choice == 4:
                print("Dot Product:", dot_product(v1, v2))
            elif choice == 5:
                print("Cross Product:", cross_product(v1, v2))
            elif choice == 9:
                print("Angle between vectors (degrees):", angle_between(v1, v2))

        elif choice == 3:
            v = np.array(list(map(float, input("Enter the vector (comma-separated): ").split(','))))
            scalar = float(input("Enter the scalar: "))
            print("Result:", scalar_multiply(v, scalar))

        elif choice == 6:
            v = np.array(list(map(float, input("Enter the vector (comma-separated): ").split(','))))
            print("Magnitude:", magnitude(v))

        elif choice == 7:
            v = np.array(list(map(float, input("Enter the vector (comma-separated): ").split(','))))
            print("Unit Vector:", unit_vector(v))

        elif choice == 8:
            v1 = np.array(list(map(float, input("Enter the vector to project (comma-separated): ").split(','))))
            v2 = np.array(list(map(float, input("Enter the vector to project onto (comma-separated): ").split(','))))
            scalar_proj, vector_proj = projection(v1, v2)
            print("Scalar Projection:", scalar_proj)
            print("Vector Projection:", vector_proj)

        elif choice == 10:
            n = int(input("Enter the number of vectors: "))
            vectors = []
            for i in range(n):
                vector = np.array(list(map(float, input(f"Enter vector {i + 1} (comma-separated): ").split(','))))
                vectors.append(vector)
            print("Resultant vector:", resultant(vectors))

        elif choice == 11:
            v1 = np.array(list(map(float, input("Enter first vector (comma-separated): ").split(','))))
            v2 = np.array(list(map(float, input("Enter second vector (comma-separated): ").split(','))))
            v3 = np.array(list(map(float, input("Enter third vector (comma-separated): ").split(','))))
            scalar_triple, vector_triple = triple_product(v1, v2, v3)
            print("Scalar Triple Product:", scalar_triple)
            print("Vector Triple Product:", vector_triple)

        elif choice == 12:
            v = np.array(list(map(float, input("Enter the vector (comma-separated): ").split(','))))
            angle = float(input("Enter the rotation angle (degrees): "))
            axis = input("Enter the rotation axis (x, y, z): ").strip().lower()
            print("Rotated Vector:", rotate_vector(v, angle, axis))

        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()
