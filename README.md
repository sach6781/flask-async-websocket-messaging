### Flask Async WebSocket Microservices
The "flask-async-websocket-microservices" project demonstrates a simple yet powerful architecture for building microservices using Flask, a popular Python web framework. The microservices communicate asynchronously through WebSocket technology, allowing for efficient and real-time data exchange.

### Key Features
Flask Framework: Leveraging the lightweight and flexible Flask framework for building microservices, ensuring simplicity and ease of development.

**Asynchronous Communication**: Harnessing the power of asynchronous programming with asyncio to achieve non-blocking communication between microservices, optimizing performance and responsiveness.

**WebSocket Integration**: Utilizing Flask-SocketIO to seamlessly integrate WebSocket support into Flask, enabling bidirectional communication for real-time updates and messaging.

**Basic CRUD Operations**: Illustrating the implementation of basic Create, Read, Update, and Delete (CRUD) operations between microservices, showcasing a foundational structure for more complex applications.

**Eventlet for Asynchronous Execution**: Employing the Eventlet library as the async_mode for Flask-SocketIO, facilitating concurrent execution of tasks and enhancing the scalability of the microservices.

### Usage
Clone the Repository:

git clone https://github.com/sach6781/flask-async-websocket-microservices.git

Run Microservices:

Navigate to the project directory.
Run each microservice individually:

python service_a.py

python service_b.py

Open Web Interface:
Open your web browser and navigate to http://127.0.0.1:5000/ for Service A and http://127.0.0.1:5001/ for Service B.
Interact with the provided web interface to observe real-time communication between the microservices.

**Contributing**
Contributions are welcome! If you have ideas for improvements, new features, or bug fixes, please submit a pull request. For major changes, please open an issue to discuss the proposed changes.

License
This project is licensed under the MIT License.

Acknowledgments
This project serves as an educational resource and a starting point for developers exploring microservices architecture with Flask and asynchronous communication through WebSockets.
