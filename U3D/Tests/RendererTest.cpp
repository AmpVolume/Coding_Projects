#include <iostream>
#include <cassert>

#include <glad/glad.h>
#include <GLFW/glfw3.h>

#include "../Engine/Renderer/Renderer.h"

using namespace Universal3D;

int main()
{
    std::cout << "Running Renderer tests...\n";

    // Initialize GLFW
    if (!glfwInit())
    {
        std::cerr << "[FAIL] GLFW initialization failed\n";
        return 1;
    }

    // Tell GLFW we're using OpenGL 3.3
    glfwWindowHint(GLFW_CONTEXT_VERSION_MAJOR, 3);
    glfwWindowHint(GLFW_CONTEXT_VERSION_MINOR, 3);
    glfwWindowHint(GLFW_OPENGL_PROFILE, GLFW_OPENGL_CORE_PROFILE);

    // Create window
    GLFWwindow* window = glfwCreateWindow(
        1280,
        720,
        "Universal3D Renderer Test",
        nullptr,
        nullptr
    );

    if (!window)
    {
        std::cerr << "[FAIL] Failed to create GLFW window\n";
        glfwTerminate();
        return 1;
    }

    glfwMakeContextCurrent(window);

    std::cout << "[PASS] GLFW window created\n";

    // Initialize Renderer
    bool initialized = Renderer::Initialize();

    assert(initialized && "Renderer::Initialize() failed");

    std::cout << "[PASS] Renderer initialized\n";

    // Render loop
    while (!glfwWindowShouldClose(window))
    {
        Renderer::BeginFrame(
            glm::vec4(0.1f, 0.2f, 0.3f, 1.0f)
        );

        Renderer::DrawTriangle();

        Renderer::EndFrame();

        glfwSwapBuffers(window);
        glfwPollEvents();
    }

    // Shutdown
    Renderer::Shutdown();

    glfwDestroyWindow(window);
    glfwTerminate();

    std::cout << "[PASS] Renderer shutdown\n";
    std::cout << "\nAll Renderer tests passed!\n";

    return 0;
}