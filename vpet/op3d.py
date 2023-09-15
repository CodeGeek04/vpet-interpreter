import open3d as o3d

def visualize(mesh):
    vis = o3d.visualization.Visualizer()
    vis.create_window()
    vis.add_geometry(mesh)
    vis.run()
    vis.destroy_window()

def main():
    mesh = o3d.io.read_triangle_mesh("monkey_smooth.obj")
    # mesh = o3d.io.read_triangle_mesh("cube.obj")
    visualize(mesh)

main()