#include <gtest/gtest.h>
#include "{{ cookiecutter.project_slug }}/example.h"

// Test fixture for {{ cookiecutter.project_slug }} library
class {{ cookiecutter.project_slug | title }}Test : public ::testing::Test {
protected:
    void SetUp() override {
        // Setup code if needed
    }

    void TearDown() override {
        // Cleanup code if needed
    }
};

// Add your tests here
TEST_F({{ cookiecutter.project_slug | title }}Test, ExampleTest) {
    EXPECT_TRUE(true);
}

TEST_F({{ cookiecutter.project_slug | title }}Test, HelloWorldTest) {
    std::string result = HelloWorld();
    EXPECT_EQ(result, "Hello, World!");
}
