import bpy
import json

data_file_path = "/your/file/path"
particle_counts = []

# TODO: if randomness involved, then define a seed for reproducibility

def count_particles(scene):
    # count number of particles at each frame
    particle_system = scene.objects["your_object"].particle_systems["its_particle_system"]
    num_particles = sum([len(particles.particles) for particles in particle_system.particles_systems])
    particle_counts.append((scene.frame_current, num_particles))
    print(f"Frame {scene.frame_current}: {num_particles} particles")

def data_export(scene):
    # write data to file at the end of the simulation
    if scene.frame_current == scene.frame_end:  # end of simulation
        with open(f"{data_file_path}_particle_counts.json", 'w') as write_file:
            write_file.write(json.dumps(particle_counts))
        print("Data exported")

# append handlers to frame_change_post
# handlers execute the appended function at every frame
bpy.app.handlers.frame_change_post.append(data_export)
bpy.app.handlers.frame_change_post.append(count_particles)

# then load data to your favorite IDE e.g. VSCode and plot with e.g. matplotlib