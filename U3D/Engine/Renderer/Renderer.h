#pragma once

#include <glm/glm.hpp>

namespace Universal3D {

class Renderer
{
public:
    static bool Initialize();

    static void BeginFrame(
        const glm::vec4& clearColor
    );

    static void EndFrame();

    static void DrawTriangle();

    static void Shutdown();
};

}