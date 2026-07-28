| Service Name | Responsibility | Endpoints | Database |

|-------------|---------------|-----------|----------|

| Course Service | Manage courses | /api/courses | courses.db |

| Student Service | Manage students | /api/students | students.db |

| API Gateway | Request routing | All APIs | None |



Synchronous Communication:

\- Immediate response

\- Tight coupling

\- Service dependency



Asynchronous Communication:

\- Uses RabbitMQ or Kafka

\- Loose coupling

\- Eventual consistency



Use RabbitMQ/Kafka for:

\- Notifications

\- Emails

\- Background jobs

\- Event-driven systems

