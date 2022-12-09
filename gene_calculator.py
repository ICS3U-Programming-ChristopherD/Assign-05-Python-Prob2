#!/usr/bin/env python3

# Created by: Chris Di Bert
# Date: Dec.9, 2022
# This program calculates all possible offspring combinations
# and their probabilities given the genotypes of the parents


# Function used to get the number of unique instances of monohybrid combinations
def monohybrid_cross(parent1, parent2):

    # Gets all possible offspring combinations
    offspring_combinations = allele_combiner_monohybrid(parent1, parent2)

    # Gets the amount of unique combinations
    homo_dom = offspring_combinations.count(parent1.upper())
    homo_rec = offspring_combinations.count(parent1.lower())
    hetero = offspring_combinations.count((parent1[0]).upper() + (parent2[0]).lower())

    # Returns unique combination quantities to main
    return homo_dom, homo_rec, hetero, offspring_combinations


# Function used to get number of unique instances of dihybrid combinations
def dihybrid_cross(parent1, parent2):

    # Creates empty list for all possible combinations
    offspring_combination = []

    # Creates allele sets for both parents
    set1 = allele_combiner_dihybrid(parent1, parent2)[0]
    set2 = allele_combiner_dihybrid(parent1, parent2)[1]

    # Crosses elements of both sets to get the offspring combinations
    for parent1_counter in range(len(set1)):
        for parent2_counter in range(len(set2)):
            combo = set1[parent1_counter] + set2[parent2_counter]
            offspring_combination.append(combo)

    # Returns all offspring combinations
    return offspring_combination


# Function used to combine parent alleles and place
# the combinations in the correct order for monohybrid crosses
def allele_combiner_monohybrid(parent1, parent2):
    parent_set = []

    # Nested for loops used to append all possible combinations to
    # the parent set
    for parent1_counter in range(2):
        for parent2_counter in range(2):
            combo = parent1[parent1_counter] + parent2[parent2_counter]
            sorted_combo = "".join(sorted(combo))
            parent_set.append(sorted_combo)

    return parent_set


# Function used to combine parent alleles and place
# the combinations in the correct order for dihybrid crosses
def allele_combiner_dihybrid(parent1, parent2):
    parent_set_1 = []
    parent_set_2 = []

    # Nested for loops used to append all possible combinations to
    # the first parent set in the correct order.

    for parent1_counter in range(2):
        for parent2_counter in range(2):
            combo = parent1[parent1_counter] + parent2[parent2_counter]
            sorted_combo = "".join(sorted(combo))
            parent_set_1.append(sorted_combo)

    # Nested for loops used to append all possible combinations to
    # the first parent set in the correct order.

    for parent2_counter in range(2, 4):
        for parent1_counter in range(2, 4):
            combo = parent1[parent1_counter] + parent2[parent2_counter]
            sorted_combo = "".join(sorted(combo))
            parent_set_2.append(sorted_combo)

    return parent_set_1, parent_set_2


# Checks for errors in parent genotypes
def parent_error_checker(parent, cross_type):

    # Error checking for monohybrid parents
    if cross_type[0] == "y":

        # Error thrown if the parent genotype exceeds 2 characters
        if len(parent) > 2:
            return -1

        # Errors thrown if the positioning of the alleles is incorrect
        elif parent[0].islower() and parent[1].isupper():
            return -2
        elif parent[0].lower() != parent[1].lower():
            return -2

        # Returns the parent if no errors were found
        else:
            return parent

    # Error checking for dihybrid parents
    else:

        # Error thrown if the parent's genotype exceeds 4 characters
        if len(parent) != 4:
            return -3

        # Errors thrown if the positioning of the alleles is incorrect
        elif parent[0].islower() and parent[1].isupper():
            return -2
        elif parent[2].islower() and parent[3].isupper():
            return -2
        elif parent[0].lower() != parent[1].lower():
            return -2

        # Returns the parent if no errors were found
        else:
            return parent


def main():

    while True:

        # Asks the user for the cross type
        print(
            '\n\n\n\n\nEnter "yes" if you want a monohybrid cross. Enter anything else for a dihybrid cross: '
        )
        cross_type = input(">> ").lower()

        # Checks if the user entered nothing

        if cross_type == "":
            print("You must enter a cross type.")
            input("Enter any key to restart: ")
            continue

        # If the user wants a monohybrid cross
        if cross_type[0] == "y":

            # Gets the user's parents and checks them for errors
            print("\n-MAKE SURE YOU ENTER CAPITALS FIRST- (e.x: Aa)")
            user_parent1 = parent_error_checker(
                input("Enter the first parent: "), cross_type
            )
            user_parent2 = parent_error_checker(
                input("Enter the second parent: "), cross_type
            )

            # Tells the user to restart if too many characters were entered
            if user_parent1 == -1 or user_parent2 == -1:
                print("No parent can exceed two charaters")
                input("Enter any key to restart: ")
                continue

            # Tells the user to restart if the alleles are entered improperly
            elif user_parent1 == -2 or user_parent2 == -2:
                print("You must enter the alleles properly")
                input("Enter any key to restart: ")
                continue

            # Result is calculated if no errors were found
            else:

                result = monohybrid_cross(user_parent1, user_parent2)

                homo_dom = result[0]
                homo_rec = result[1]
                hetero = result[2]

                print(
                    f"There is a {homo_dom / 4 * 100}% chance of homozygous dominant ({homo_dom}:4 = {user_parent1[0].upper()}{user_parent1[0].upper()})"
                )
                print(
                    f"There is a {homo_rec / 4 * 100}% chance of homozygous recessive ({homo_rec}:4 = {user_parent1[0].lower()}{user_parent1[0].lower()})"
                )
                print(
                    f"There is a {hetero / 4 * 100}% chance of heterozygous. ({hetero}:4 = {user_parent1[0].upper()}{user_parent1[0].lower()})"
                )

        # If the user wants a dihybrid cross
        else:

            # Gets the user's parents and checks them for errors
            user_parent1 = input("Enter the first parent: ")
            user_parent2 = input("Enter the second parent: ")

            # Calls the error checker function
            user_parent1 = parent_error_checker(user_parent1, cross_type)
            user_parent2 = parent_error_checker(user_parent2, cross_type)

            # Tells the user to restart if too many characters were entered
            if user_parent1 == -3 or user_parent2 == -3:
                print("All parents must be 4 characters")
                input("Enter any key to restart: ")
                continue

            # Tells the user to restart if the alleles are entered improperly
            elif user_parent1 == -2 or user_parent2 == -2:
                print("You must enter the alleles properly")
                input("Enter any key to restart: ")
                continue

            # Result is calculated if no errors were found
            else:

                # List to hold the numbers of a given combination
                combo_count = []

                # Gets all combinations from DihybridCross function
                combinations = dihybrid_cross(user_parent1, user_parent2)

                # Prints all genotype possibilities including their duplicates
                print("\nALL GENOTYPES:")
                print(f"{combinations}\n")

                # List of all distinct possible genotypes
                unique_combinatons = list(set(combinations))

                # Prints all distinct possible genotypes
                print("\nUNIQUE GENOTYPES:")
                print(f"{unique_combinatons}\n\n")

                # Prints each genotype, the chance that the offspring will inherit it,
                # and its frequency in the cross.
                print("GENOTYPIC RATIOS:\n")
                for counter in range(len(unique_combinatons)):
                    combo_count = combinations.count(unique_combinatons[counter])
                    print(
                        f"{unique_combinatons[counter]} - {combo_count / 16 * 100}% ({combo_count}:16)."
                    )

        # Asks the user if they would like to restart
        restart = input("Enter 'y' if you would like to restart: ").lower()
        if restart == "":
            continue
        if restart[0] == "y":
            continue
        else:
            break


if __name__ == "__main__":
    main()
