def hanoi_solver(n):
    # Initialize three rods
    source = list(range(n, 0, -1))  # [n, n-1, ..., 1]
    auxiliary = []
    destination = []

    # Function to format rod state
    def format_rod(rod):
        if not rod:
            return "[]"
        return f"[{', '.join(str(x) for x in rod)}]"

    # List to store all states
    moves = [f"{format_rod(source)} {format_rod(auxiliary)} {format_rod(destination)}"]

    def move_disks(num_disks, from_rod, to_rod, aux_rod):
        if num_disks == 1:
            # Move the disk
            to_rod.append(from_rod.pop())
            # Record the state
            moves.append(f"{format_rod(source)} {format_rod(auxiliary)} {format_rod(destination)}")
            return

        # Move n-1 disks to auxiliary
        move_disks(num_disks - 1, from_rod, aux_rod, to_rod)
        # Move bottom disk to destination
        move_disks(1, from_rod, to_rod, aux_rod)
        # Move n-1 disks from auxiliary to destination
        move_disks(num_disks - 1, aux_rod, to_rod, from_rod)

    # Solve for n disks
    move_disks(n, source, destination, auxiliary)

    return "\n".join(moves)
