import { Request, Response, NextFunction } from 'express';
import { getUserData, addUser } from '../../src/controllers/userController';
import User from '../../src/models/userModel';

jest.mock('../../src/models/userModel');

describe('User Controller', () => {
    let req: Partial<Request>;
    let res: Partial<Response>;
    let next: NextFunction;

    beforeEach(() => {
        req = {
            body: {}
        };
        res = {
            status: jest.fn().mockReturnThis(),
            json: jest.fn(),
        };
        next = jest.fn();
        jest.clearAllMocks();
    });

    describe('getUserData', () => {
        it('should return user data when user exists', async () => {
            const mockUser = { name: 'Test User' };
            (User.findOne as jest.Mock).mockResolvedValue(mockUser);

            await getUserData(req as Request, res as Response, next);

            expect(User.findOne).toHaveBeenCalled();
            expect(res.status).toHaveBeenCalledWith(200);
            expect(res.json).toHaveBeenCalledWith(mockUser);
        });

        it('should return 404 error when no user exists', async () => {
            (User.findOne as jest.Mock).mockResolvedValue(null);

            await getUserData(req as Request, res as Response, next);

            expect(User.findOne).toHaveBeenCalled();
            expect(res.status).toHaveBeenCalledWith(404);
            // Since express-async-handler catches the error, it calls next(error)
            expect(next).toHaveBeenCalledWith(expect.any(Error));
            const error = (next as jest.Mock).mock.calls[0][0];
            expect(error.message).toBe('There are no user in the DB');
        });
    });

    describe('addUser', () => {
        const validUserBody = {
            fullName: 'John Doe',
            shortname: 'John',
            email: 'john@example.com',
            password: 'password123',
            about: 'About me',
            age: 30,
            address: '123 Main St',
            languages: ['English'],
            phone: '1234567890',
            jobTitle: 'Developer',
            education: [{ degree: 'BS' }]
        };

        it('should add a new user when all fields are present and no user exists', async () => {
            req.body = validUserBody;
            (User.findOne as jest.Mock).mockResolvedValue(null);
            
            // Mocking the instance handling is tricky with default export mocks usually
            // but since we are just testing the controller logic calling new User(),
            // we can mock the implementation of User if needed, or better, 
            // since we mocked the module, User is a mock constructor.
            // We need to make sure the instance created has a save method.
            
            const mockSavedUser = { ...validUserBody, _id: '123' };
            const saveMock = jest.fn().mockResolvedValue(mockSavedUser);
            
            // Allow User constructor to return an object with save method
            (User as unknown as jest.Mock).mockImplementation(() => ({
                save: saveMock
            }));

            await addUser(req as Request, res as Response, next);

            expect(User.findOne).toHaveBeenCalled();
            expect(saveMock).toHaveBeenCalled();
            expect(res.status).toHaveBeenCalledWith(201);
            expect(res.json).toHaveBeenCalledWith({
                message: "User Added successfully",
                user: mockSavedUser
            });
        });

        it('should throw error if fields are invalid/missing', async () => {
            req.body = { ...validUserBody, email: undefined }; // Missing email

            await addUser(req as Request, res as Response, next);

            expect(next).toHaveBeenCalledWith(expect.any(Error));
            const error = (next as jest.Mock).mock.calls[0][0];
            expect(error.message).toBe('All fields are required');
            expect(User.findOne).not.toHaveBeenCalled();
        });

        it('should return 409 if user already exists', async () => {
            req.body = validUserBody;
            // Existing user found
            (User.findOne as jest.Mock).mockResolvedValue({ some: 'user' });

            await addUser(req as Request, res as Response, next);

            expect(User.findOne).toHaveBeenCalled();
            expect(res.status).toHaveBeenCalledWith(409);
            expect(next).toHaveBeenCalledWith(expect.any(Error));
            const error = (next as jest.Mock).mock.calls[0][0];
            expect(error.message).toBe('One user exists in the Database');
        });
    });
});
