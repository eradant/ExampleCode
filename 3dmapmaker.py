def generate_3d_model(dem_file, output_file, output_format='stl'):
    # Load DEM data
    with rasterio.open(dem_file) as src:
        dem_data = src.read(1)
        transform = src.transform

    # Generate vertices and faces
    x, y = np.meshgrid(np.arange(dem_data.shape[1]), np.arange(dem_data.shape[0]))
    z = dem_data
    vertices = np.vstack([x.ravel(), y.ravel(), z.ravel()]).T

    faces = []
    for i in range(dem_data.shape[0] - 1):
        for j in range(dem_data.shape[1] - 1):
            faces.append([i * dem_data.shape[1] + j, (i + 1) * dem_data.shape[1] + j, i * dem_data.shape[1] + (j + 1)])
            faces.append([(i + 1) * dem_data.shape[1] + j, (i + 1) * dem_data.shape[1] + (j + 1), i * dem_data.shape[1] + (j + 1)])
    faces = np.array(faces)

    # Export the 3D model
    if output_format == 'stl':
        from stl import mesh
        terrain_mesh = mesh.Mesh(np.zeros(faces.shape[0], dtype=mesh.Mesh.dtype))
        for i, f in enumerate(faces):
            for j in range(3):
                terrain_mesh.vectors[i][j] = vertices[f[j]]
        terrain_mesh.save(output_file)
    elif output_format == '3mf':
        import py3mf
        model = py3mf.Model()
        mesh3mf = model.resources.add_mesh()
        mesh3mf.vertices = vertices
        mesh3mf.triangles = faces
        model.save(output_file)
    else:
        raise ValueError("Unsupported format. Use 'stl' or '3mf'.")

# Example usage
generate_3d_model('path_to_dem_file.tif', 'output_model.stl', 'stl')