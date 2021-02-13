# Orbital Visualizer
Visualizer of orbits and proximal objects on varying frequencies.

### Prerequisites

To run visualizer.py you will need [Pyhton 3.0+](https://www.python.org/) and [Pygame](https://www.pygame.org/news)

## Objects

Star Objects:
* coords - (x,y) starting coords
* size - object radius in pixels
* eg: SUN = Star((x,y), r)

Planet Objects:
* Ocoords - (x,y) tuple of the coordinates this planet orbits
* Oradius - radius around which the planet orbits
* velocity - speed at which it orbits (completes one rotation)
* size - size (radius) of this planet in pixels
* col - color of planet
* distline - bool, show distance lines to other planets
* eg: EARTH = Planet(SUN.coords, 100, 3, 12, BLUE, True)

## Authors

* **Rohan Dawar**

## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details
