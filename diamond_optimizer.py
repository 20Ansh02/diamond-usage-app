class Diamond:
    def __init__(self, size, status='new'):
        self.size = size
        self.status = status  # 'new' or 'returned'

class NecklaceDesign:
    def __init__(self, name, required_diamonds):
        self.name = name
        self.required_diamonds = required_diamonds  # Dictionary of {diamond_size: quantity}

class DiamondManager:
    diamonds = []

    @classmethod
    def add_diamond(cls, size, status='new'):
        diamond = Diamond(size, status)
        cls.diamonds.append(diamond)

    @classmethod
    def get_available_diamonds(cls):
        # Sort diamonds by size in descending order
        return sorted(cls.diamonds, key=lambda x: x.size, reverse=True)

class NecklaceDesignManager:
    necklace_designs = []

    @classmethod
    def create_necklace_design(cls, name, required_diamonds):
        necklace_design = NecklaceDesign(name, required_diamonds)
        cls.necklace_designs.append(necklace_design)

class DiamondUsageOptimizer:
    @staticmethod
    def optimize_usage():
        available_diamonds = DiamondManager.get_available_diamonds()
        total_necklaces_crafted = 0

        # Initialize remaining quantity of each diamond size
        remaining_quantity = {diamond.size: sum(1 for d in available_diamonds if d.size == diamond.size) for diamond in available_diamonds}

        # Iterate through necklace designs
        for necklace_design in NecklaceDesignManager.necklace_designs:
            diamonds_used = {}

            # Iterate through required diamond sizes
            for size, quantity in necklace_design.required_diamonds.items():
                diamonds_used[size] = 0  # Initialize diamonds used for current size

                # Check if there are returned diamonds of required size
                if remaining_quantity.get(size, 0) > 0:
                    returned_diamonds = [diamond for diamond in available_diamonds if diamond.size == size and diamond.status == 'returned']
                    used_returned = min(len(returned_diamonds), quantity)

                    # Update diamonds used and remaining quantity
                    diamonds_used[size] += used_returned
                    remaining_quantity[size] -= used_returned
                    total_necklaces_crafted += 1

                # Check for new diamonds if needed
                if diamonds_used[size] < quantity:
                    deficit = quantity - diamonds_used[size]
                    new_diamonds = [diamond for diamond in available_diamonds if diamond.size == size and diamond.status == 'new']
                    used_new = min(len(new_diamonds), deficit)

                    # Update diamonds used and remaining quantity
                    diamonds_used[size] += used_new
                    remaining_quantity[size] -= used_new

        return total_necklaces_crafted

# Example usage:
DiamondManager.add_diamond(size=0.5)
DiamondManager.add_diamond(size=0.75, status='returned')
DiamondManager.add_diamond(size=1.0)

NecklaceDesignManager.create_necklace_design(name='Simple Necklace', required_diamonds={0.5: 1, 1.0: 2})
NecklaceDesignManager.create_necklace_design(name='Fancy Necklace', required_diamonds={0.75: 3, 1.0: 1})

total_necklaces_crafted = DiamondUsageOptimizer.optimize_usage()
print("Total necklaces crafted:", total_necklaces_crafted)
