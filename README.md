# Cloudflare WARP Manager

WARP Manager is a portable application for Windows that enables automatic IP address switching and management through the Cloudflare WARP service. This tool is designed to enhance your online privacy and security by allowing users to seamlessly change their IP addresses without the need for installation.

## Application Screenshot 

![Ekran görüntüsü 2025-02-22 004146](https://github.com/user-attachments/assets/3b4f8929-d737-42bb-a9b2-fad6e5f11677)

## Features

 -   Real-Time IP Address Tracking: Monitor your current IP address dynamically as it changes.
 -   Manual and Automatic IP Reset: Instantly change your IP address with a single click or set an automatic reset interval.
 -   Customizable Refresh Interval: Choose the frequency of automatic IP resets, with options ranging from 1 to 10 minutes.
 -   IP History List: Keep track of your last 10 IP addresses for easy reference and review.
 -   System Tray Functionality: Run the application in the background with system tray support, allowing you to minimize it while you work.
 -   Simple and User-Friendly Interface: Designed for ease of use, ensuring that users of all levels can navigate and operate the application effortlessly.

## Requirements

 -   PyQt6==6.4.2
 -   requests==2.31.0

## Installation

Note: WARP Manager is a portable application that does not require installation. However, it requires the Cloudflare WARP client to be installed on your system. To set up, ensure that you have the Cloudflare WARP client installed:

  -  Download the Cloudflare WARP client from the Cloudflare Official Website.
  -  Follow the installation instructions provided on their site.

## Usage

WARP Manager is straightforward to use:

 -   Manual Reset: To change your IP address immediately, click the "Manual IP Reset" button on the main interface.
 -   Automatic Mode: Start the automatic IP reset by clicking the "Start" button, allowing your IP to change at the defined intervals.
 -   IP Tracking: The main window displays your current IP address and maintains a list of your recent IP addresses for reference.

## Development

We welcome contributions! To contribute to the WARP Manager project, please follow these steps:

 -   Fork the repository on GitHub.
 -   Create a new branch for your feature (e.g., git checkout -b feature/your-feature).
 -   Make your changes and commit them.
 -   Push your changes to your forked repository (e.g., git push origin feature/your-feature).
 -   Open a Pull Request on the original repository to propose your changes.

## License

This project is licensed under the MIT License. For more details, please refer to the LICENSE file included in the repository.

Note: This application is not an official Cloudflare product. It is designed to work in conjunction with the Cloudflare WARP client for enhanced IP management and security.
