#include <iostream>
#include <glm/glm.hpp>
#include "../Engine/Math/Transform.h"

int main()
{
    Universal3D::Transform transform;

    transform.position = glm::vec3(10.0f, 5.0f, 2.0f);
    transform.rotation = glm::vec3(0.0f, 90.0f, 0.0f);
    transform.scale = glm::vec3(2.0f, 2.0f, 2.0f);

    glm::mat4 matrix = transform.GetMatrix();

    std::cout << "Transform Matrix:\n";

    for (int row = 0; row < 4; ++row)
    {
        for (int column = 0; column < 4; ++column)
        {
            std::cout << matrix[column][row] << " ";
        }

        std::cout << '\n';
    }

    return 0;
}