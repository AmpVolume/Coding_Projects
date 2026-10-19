#include "Renderer.h"

#include <glad/glad.h>
#include <GLFW/glfw3.h>

namespace Universal3D {

bool Renderer::Initialize()
{
    if (!gladLoadGLLoader(
        reinterpret_cast<GLADloadproc>(glfwGetProcAddress)))
    {
        return false;
    }

    glEnable(GL_DEPTH_TEST);

    return true;
}

void Renderer::BeginFrame(
    const glm::vec4& clearColor
)
{
    glClearColor(
        clearColor.r,
        clearColor.g,
        clearColor.b,
        clearColor.a
    );

    glClear(
        GL_COLOR_BUFFER_BIT |
        GL_DEPTH_BUFFER_BIT
    );
}

void Renderer::EndFrame()
{
}

void Renderer::DrawTriangle()
{
    glBegin(GL_TRIANGLES);

    glVertex3f(-0.5f, -0.5f, 0.0f);
    glVertex3f( 0.5f, -0.5f, 0.0f);
    glVertex3f( 0.0f,  0.5f, 0.0f);

    glEnd();
}

void Renderer::Shutdown()
{
}

}