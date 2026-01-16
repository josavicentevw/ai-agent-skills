# React/TypeScript Stack-Specific Rules

This document provides React and TypeScript-specific validation rules for code reviews. These rules supplement the general checklists and should be applied when reviewing React/TypeScript code.

**Quick resources:** [Cheat Sheet](./concise/react-typescript-concise.md) · [Code Examples](./examples-only/react-typescript-examples.md)

---

## 1. TypeScript Strict Mode Requirements {#typescript-strict}

### Avoid `any` Type
- [ ] No usage of `any` type unless absolutely necessary with justification comment
- [ ] Use `unknown` instead of `any` for truly dynamic types
- [ ] Define proper interfaces/types for external data
- [ ] Use type guards for narrowing `unknown` types
- [ ] Enable `strict` mode in `tsconfig.json`

**Examples:**
```typescript
// ❌ BAD - Using any without justification
function processData(data: any) {
  return data.value * 2;
}

// ❌ BAD - Any in function parameters
const handleClick = (event: any) => {
  console.log(event.target.value);
};

// ✅ GOOD - Proper type definition
interface ProcessableData {
  value: number;
  metadata?: Record<string, string>;
}

function processData(data: ProcessableData): number {
  return data.value * 2;
}

// ✅ GOOD - Proper event typing
const handleClick = (event: React.ChangeEvent<HTMLInputElement>) => {
  console.log(event.target.value);
};

// ✅ ACCEPTABLE - Using any with justification
interface LegacyApiResponse {
  // Using any here because legacy API returns dynamic structure
  // that varies by endpoint. Will be replaced when API v2 is available.
  // TODO: Replace with proper types when migrating to API v2 (ticket: PROJ-456)
  data: any;
  status: number;
}
```

### Type Inference and Explicit Types
- [ ] Let TypeScript infer simple types (don't over-annotate)
- [ ] Explicitly type function return values for public APIs
- [ ] Use type assertions sparingly with `as` keyword
- [ ] Prefer type guards over type assertions
- [ ] Use generics for reusable type-safe functions

**Examples:**
```typescript
// ❌ BAD - Unnecessary type annotations
const count: number = 5;
const name: string = "John";
const items: string[] = ["a", "b", "c"];

// ✅ GOOD - Let TypeScript infer
const count = 5;
const name = "John";
const items = ["a", "b", "c"];

// ✅ GOOD - Explicit return type for public API
export function calculateTotal(items: CartItem[]): number {
  return items.reduce((sum, item) => sum + item.price * item.quantity, 0);
}

// ✅ GOOD - Generic function
function groupBy<T, K extends keyof T>(items: T[], key: K): Record<string, T[]> {
  return items.reduce((groups, item) => {
    const groupKey = String(item[key]);
    return {
      ...groups,
      [groupKey]: [...(groups[groupKey] || []), item]
    };
  }, {} as Record<string, T[]>);
}

// ✅ GOOD - Type guard instead of assertion
function isUser(value: unknown): value is User {
  return (
    typeof value === 'object' &&
    value !== null &&
    'id' in value &&
    'name' in value
  );
}

// Usage
const data: unknown = await fetchData();
if (isUser(data)) {
  console.log(data.name); // TypeScript knows data is User
}
```

---

## 2. React Hooks Rules {#react-hooks}

### Dependency Arrays
- [ ] All dependencies used in effect included in dependency array
- [ ] No missing dependencies (ESLint rule `react-hooks/exhaustive-deps` enabled)
- [ ] No unnecessary dependencies causing extra renders
- [ ] Use `useCallback` for function dependencies in effects
- [ ] Use `useMemo` for computed values used as dependencies

**Examples:**
```typescript
// ❌ BAD - Missing dependencies
const [count, setCount] = useState(0);
const [multiplier, setMultiplier] = useState(2);

useEffect(() => {
  const result = count * multiplier;
  console.log(result);
}, [count]); // Missing multiplier dependency

// ❌ BAD - Unnecessary object/array recreation causing extra renders
useEffect(() => {
  fetchData({ filter: 'active' });
}, [{ filter: 'active' }]); // New object on every render

// ✅ GOOD - All dependencies included
useEffect(() => {
  const result = count * multiplier;
  console.log(result);
}, [count, multiplier]);

// ✅ GOOD - Using useMemo for object dependencies
const filterOptions = useMemo(() => ({ filter: 'active' }), []);

useEffect(() => {
  fetchData(filterOptions);
}, [filterOptions]);

// ✅ GOOD - Using useCallback for function dependencies
const handleDataUpdate = useCallback((newData: Data) => {
  setData(newData);
  logUpdate(newData);
}, []); // Empty deps if it doesn't depend on state

useEffect(() => {
  const subscription = dataService.subscribe(handleDataUpdate);
  return () => subscription.unsubscribe();
}, [handleDataUpdate]);
```

### Custom Hooks
- [ ] Custom hooks start with `use` prefix
- [ ] Custom hooks encapsulate reusable stateful logic
- [ ] Custom hooks follow Rules of Hooks
- [ ] Custom hooks have clear, focused responsibility
- [ ] Custom hooks are properly typed with TypeScript

**Examples:**
```typescript
// ✅ GOOD - Custom hook for API fetching
interface UseFetchResult<T> {
  data: T | null;
  loading: boolean;
  error: Error | null;
  refetch: () => void;
}

function useFetch<T>(url: string): UseFetchResult<T> {
  const [data, setData] = useState<T | null>(null);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState<Error | null>(null);

  const fetchData = useCallback(async () => {
    setLoading(true);
    setError(null);
    
    try {
      const response = await fetch(url);
      if (!response.ok) {
        throw new Error(`HTTP error! status: ${response.status}`);
      }
      const json = await response.json();
      setData(json);
    } catch (e) {
      setError(e instanceof Error ? e : new Error('Unknown error'));
    } finally {
      setLoading(false);
    }
  }, [url]);

  useEffect(() => {
    fetchData();
  }, [fetchData]);

  return { data, loading, error, refetch: fetchData };
}

// ✅ GOOD - Custom hook for form management
interface UseFormResult<T> {
  values: T;
  errors: Partial<Record<keyof T, string>>;
  handleChange: (field: keyof T) => (e: React.ChangeEvent<HTMLInputElement>) => void;
  handleSubmit: (onSubmit: (values: T) => void) => (e: React.FormEvent) => void;
  reset: () => void;
}

function useForm<T extends Record<string, any>>(
  initialValues: T,
  validate?: (values: T) => Partial<Record<keyof T, string>>
): UseFormResult<T> {
  const [values, setValues] = useState<T>(initialValues);
  const [errors, setErrors] = useState<Partial<Record<keyof T, string>>>({});

  const handleChange = useCallback((field: keyof T) => {
    return (e: React.ChangeEvent<HTMLInputElement>) => {
      setValues(prev => ({ ...prev, [field]: e.target.value }));
    };
  }, []);

  const handleSubmit = useCallback((onSubmit: (values: T) => void) => {
    return (e: React.FormEvent) => {
      e.preventDefault();
      
      const validationErrors = validate?.(values) || {};
      setErrors(validationErrors);
      
      if (Object.keys(validationErrors).length === 0) {
        onSubmit(values);
      }
    };
  }, [values, validate]);

  const reset = useCallback(() => {
    setValues(initialValues);
    setErrors({});
  }, [initialValues]);

  return { values, errors, handleChange, handleSubmit, reset };
}
```

### Hook Rules
- [ ] Only call hooks at the top level (not in loops, conditions, or nested functions)
- [ ] Only call hooks from React functions (components or custom hooks)
- [ ] Use ESLint plugin `eslint-plugin-react-hooks`
- [ ] Clean up effects with return function when needed
- [ ] Avoid infinite loops in useEffect

**Examples:**
```typescript
// ❌ BAD - Conditional hook call
function UserProfile({ userId }: { userId: string | null }) {
  if (userId) {
    const user = useFetch<User>(`/api/users/${userId}`); // Hook called conditionally
    return <div>{user.data?.name}</div>;
  }
  return null;
}

// ✅ GOOD - Hook called unconditionally
function UserProfile({ userId }: { userId: string | null }) {
  const shouldFetch = userId !== null;
  const url = shouldFetch ? `/api/users/${userId}` : '';
  const user = useFetch<User>(url);

  if (!userId) {
    return null;
  }

  return <div>{user.data?.name}</div>;
}

// ✅ GOOD - Cleanup in useEffect
useEffect(() => {
  const controller = new AbortController();
  
  async function fetchData() {
    try {
      const response = await fetch(url, { signal: controller.signal });
      const data = await response.json();
      setData(data);
    } catch (error) {
      if (error.name !== 'AbortError') {
        setError(error);
      }
    }
  }
  
  fetchData();
  
  // Cleanup function
  return () => {
    controller.abort();
  };
}, [url]);
```

---

## 3. Component Patterns {#component-patterns}

### Functional Components
- [ ] Use functional components (not class components)
- [ ] Define prop interfaces with TypeScript
- [ ] Use React.FC sparingly (prefer explicit prop typing)
- [ ] Export component and prop interface
- [ ] Use default props appropriately

**Examples:**
```typescript
// ❌ BAD - Using React.FC (discouraged in newer React)
const Button: React.FC<{ label: string }> = ({ label }) => {
  return <button>{label}</button>;
};

// ✅ GOOD - Explicit prop typing
interface ButtonProps {
  label: string;
  onClick?: () => void;
  variant?: 'primary' | 'secondary';
  disabled?: boolean;
}

export function Button({ 
  label, 
  onClick, 
  variant = 'primary',
  disabled = false 
}: ButtonProps) {
  return (
    <button
      onClick={onClick}
      disabled={disabled}
      className={`btn btn-${variant}`}
    >
      {label}
    </button>
  );
}

// ✅ GOOD - Component with children
interface CardProps {
  title: string;
  children: React.ReactNode;
  footer?: React.ReactNode;
}

export function Card({ title, children, footer }: CardProps) {
  return (
    <div className="card">
      <div className="card-header">
        <h3>{title}</h3>
      </div>
      <div className="card-body">
        {children}
      </div>
      {footer && (
        <div className="card-footer">
          {footer}
        </div>
      )}
    </div>
  );
}

// ✅ GOOD - Generic component
interface ListProps<T> {
  items: T[];
  renderItem: (item: T, index: number) => React.ReactNode;
  keyExtractor: (item: T) => string | number;
  emptyMessage?: string;
}

export function List<T>({ 
  items, 
  renderItem, 
  keyExtractor,
  emptyMessage = 'No items found'
}: ListProps<T>) {
  if (items.length === 0) {
    return <div className="empty-state">{emptyMessage}</div>;
  }

  return (
    <ul>
      {items.map((item, index) => (
        <li key={keyExtractor(item)}>
          {renderItem(item, index)}
        </li>
      ))}
    </ul>
  );
}
```

### Component Composition
- [ ] Favor composition over inheritance
- [ ] Use children prop for flexible layouts
- [ ] Create reusable, single-responsibility components
- [ ] Use render props or custom hooks for sharing logic
- [ ] Keep components focused and testable

**Examples:**
```typescript
// ✅ GOOD - Composition with children
interface ModalProps {
  isOpen: boolean;
  onClose: () => void;
  children: React.ReactNode;
}

export function Modal({ isOpen, onClose, children }: ModalProps) {
  if (!isOpen) return null;

  return (
    <div className="modal-overlay" onClick={onClose}>
      <div className="modal-content" onClick={(e) => e.stopPropagation()}>
        {children}
      </div>
    </div>
  );
}

// Usage
function App() {
  return (
    <Modal isOpen={isOpen} onClose={handleClose}>
      <ModalHeader>
        <h2>Confirm Action</h2>
      </ModalHeader>
      <ModalBody>
        <p>Are you sure you want to proceed?</p>
      </ModalBody>
      <ModalFooter>
        <Button onClick={handleClose}>Cancel</Button>
        <Button onClick={handleConfirm} variant="primary">Confirm</Button>
      </ModalFooter>
    </Modal>
  );
}
```

---

## 4. State Management {#state-management}

### useState Best Practices
- [ ] Use multiple useState calls for independent state
- [ ] Use single useState with object for related state
- [ ] Initialize state with proper types
- [ ] Use functional updates when new state depends on previous state
- [ ] Avoid storing derived state (use useMemo instead)

**Examples:**
```typescript
// ❌ BAD - Single state for unrelated values
const [state, setState] = useState({
  count: 0,
  userName: '',
  isLoading: false
});

// ✅ GOOD - Separate state for independent values
const [count, setCount] = useState(0);
const [userName, setUserName] = useState('');
const [isLoading, setIsLoading] = useState(false);

// ✅ GOOD - Single state for related values
interface FormState {
  email: string;
  password: string;
  rememberMe: boolean;
}

const [formState, setFormState] = useState<FormState>({
  email: '',
  password: '',
  rememberMe: false
});

// ❌ BAD - Not using functional update
const increment = () => {
  setCount(count + 1); // May use stale value
};

// ✅ GOOD - Functional update
const increment = () => {
  setCount(prevCount => prevCount + 1);
};

// ❌ BAD - Storing derived state
const [items, setItems] = useState<Item[]>([]);
const [itemCount, setItemCount] = useState(0); // Derived from items

// ✅ GOOD - Computing derived state
const [items, setItems] = useState<Item[]>([]);
const itemCount = items.length; // Or use useMemo if expensive
```

### useEffect Best Practices
- [ ] Use separate useEffect hooks for different concerns
- [ ] Return cleanup function when needed
- [ ] Avoid putting too much logic in useEffect
- [ ] Extract complex logic to custom hooks or utility functions
- [ ] Use useLayoutEffect only when measuring DOM before paint

**Examples:**
```typescript
// ❌ BAD - Multiple concerns in single effect
useEffect(() => {
  // Concern 1: Fetch data
  fetchUserData(userId).then(setUser);
  
  // Concern 2: Setup event listener
  window.addEventListener('resize', handleResize);
  
  // Concern 3: Update document title
  document.title = `User ${userId}`;
}, [userId]);

// ✅ GOOD - Separate effects for different concerns
useEffect(() => {
  fetchUserData(userId).then(setUser);
}, [userId]);

useEffect(() => {
  window.addEventListener('resize', handleResize);
  return () => window.removeEventListener('resize', handleResize);
}, []);

useEffect(() => {
  document.title = `User ${userId}`;
  return () => { document.title = 'App'; };
}, [userId]);
```

### Context API
- [ ] Use Context for truly global state (theme, auth, localization)
- [ ] Don't overuse Context (prefer prop drilling for 1-2 levels)
- [ ] Split contexts by concern (don't create massive global context)
- [ ] Memoize context value to prevent unnecessary re-renders
- [ ] Provide TypeScript types for context value

**Examples:**
```typescript
// ✅ GOOD - Typed context with provider
interface AuthContextValue {
  user: User | null;
  login: (credentials: Credentials) => Promise<void>;
  logout: () => void;
  isAuthenticated: boolean;
}

const AuthContext = createContext<AuthContextValue | undefined>(undefined);

export function AuthProvider({ children }: { children: React.ReactNode }) {
  const [user, setUser] = useState<User | null>(null);

  const login = useCallback(async (credentials: Credentials) => {
    const userData = await authService.login(credentials);
    setUser(userData);
  }, []);

  const logout = useCallback(() => {
    authService.logout();
    setUser(null);
  }, []);

  const value = useMemo(() => ({
    user,
    login,
    logout,
    isAuthenticated: user !== null
  }), [user, login, logout]);

  return <AuthContext.Provider value={value}>{children}</AuthContext.Provider>;
}

// ✅ GOOD - Custom hook for context consumption
export function useAuth(): AuthContextValue {
  const context = useContext(AuthContext);
  if (context === undefined) {
    throw new Error('useAuth must be used within an AuthProvider');
  }
  return context;
}

// Usage
function UserProfile() {
  const { user, logout } = useAuth();
  
  return (
    <div>
      <p>Welcome, {user?.name}</p>
      <button onClick={logout}>Logout</button>
    </div>
  );
}
```

---

## 5. HTTP Client Requirements {#http-client}

### Timeouts and Abort Controllers
- [ ] All HTTP requests have explicit timeouts
- [ ] Use AbortController for cancellable requests
- [ ] Clean up aborted requests in useEffect
- [ ] Handle timeout errors appropriately
- [ ] Configure default timeout in HTTP client

**Examples:**
```typescript
// ❌ BAD - No timeout
async function fetchUser(id: string): Promise<User> {
  const response = await fetch(`/api/users/${id}`);
  return response.json();
}

// ✅ GOOD - With timeout and AbortController
async function fetchUser(id: string, timeoutMs: number = 5000): Promise<User> {
  const controller = new AbortController();
  const timeoutId = setTimeout(() => controller.abort(), timeoutMs);

  try {
    const response = await fetch(`/api/users/${id}`, {
      signal: controller.signal
    });
    
    if (!response.ok) {
      throw new Error(`HTTP error! status: ${response.status}`);
    }
    
    return await response.json();
  } catch (error) {
    if (error.name === 'AbortError') {
      throw new TimeoutError(`Request timeout after ${timeoutMs}ms`);
    }
    throw error;
  } finally {
    clearTimeout(timeoutId);
  }
}

// ✅ GOOD - Using axios with timeout
import axios from 'axios';

const apiClient = axios.create({
  baseURL: process.env.REACT_APP_API_URL,
  timeout: 10000, // 10 seconds default
  headers: {
    'Content-Type': 'application/json'
  }
});

// ✅ GOOD - In React component with cleanup
function UserProfile({ userId }: { userId: string }) {
  const [user, setUser] = useState<User | null>(null);
  const [error, setError] = useState<Error | null>(null);

  useEffect(() => {
    const controller = new AbortController();

    async function loadUser() {
      try {
        const response = await fetch(`/api/users/${userId}`, {
          signal: controller.signal,
          headers: { 'Accept': 'application/json' }
        });
        
        if (!response.ok) throw new Error('Failed to fetch user');
        
        const data = await response.json();
        setUser(data);
      } catch (err) {
        if (err.name !== 'AbortError') {
          setError(err instanceof Error ? err : new Error('Unknown error'));
        }
      }
    }

    loadUser();

    return () => {
      controller.abort(); // Cleanup on unmount
    };
  }, [userId]);

  if (error) return <div>Error: {error.message}</div>;
  if (!user) return <div>Loading...</div>;
  
  return <div>{user.name}</div>;
}
```

### Error Handling
- [ ] Create custom error classes for different error types
- [ ] Handle network errors separately from HTTP errors
- [ ] Provide user-friendly error messages
- [ ] Log errors with sufficient context
- [ ] Implement retry logic for transient failures

**Examples:**
```typescript
// ✅ GOOD - Custom error classes
export class ApiError extends Error {
  constructor(
    message: string,
    public statusCode: number,
    public response?: any
  ) {
    super(message);
    this.name = 'ApiError';
  }
}

export class NetworkError extends Error {
  constructor(message: string, public cause?: Error) {
    super(message);
    this.name = 'NetworkError';
  }
}

export class TimeoutError extends Error {
  constructor(message: string) {
    super(message);
    this.name = 'TimeoutError';
  }
}

// ✅ GOOD - Comprehensive error handling
async function apiRequest<T>(
  url: string,
  options?: RequestInit
): Promise<T> {
  const controller = new AbortController();
  const timeoutId = setTimeout(() => controller.abort(), 10000);

  try {
    const response = await fetch(url, {
      ...options,
      signal: controller.signal
    });

    if (!response.ok) {
      const errorData = await response.json().catch(() => null);
      throw new ApiError(
        errorData?.message || `HTTP ${response.status}`,
        response.status,
        errorData
      );
    }

    return await response.json();
  } catch (error) {
    if (error instanceof ApiError) {
      throw error;
    }
    
    if (error.name === 'AbortError') {
      throw new TimeoutError('Request timeout');
    }
    
    if (error instanceof TypeError) {
      throw new NetworkError('Network error - please check your connection', error);
    }
    
    throw error;
  } finally {
    clearTimeout(timeoutId);
  }
}

// ✅ GOOD - Error handling in component
function DataDisplay() {
  const [data, setData] = useState<Data | null>(null);
  const [error, setError] = useState<string | null>(null);

  useEffect(() => {
    async function loadData() {
      try {
        const result = await apiRequest<Data>('/api/data');
        setData(result);
        setError(null);
      } catch (err) {
        if (err instanceof TimeoutError) {
          setError('Request took too long. Please try again.');
        } else if (err instanceof NetworkError) {
          setError('Network error. Please check your internet connection.');
        } else if (err instanceof ApiError && err.statusCode === 404) {
          setError('Data not found.');
        } else {
          setError('An unexpected error occurred. Please try again.');
        }
        
        console.error('Failed to load data:', err);
      }
    }

    loadData();
  }, []);

  if (error) return <ErrorMessage message={error} />;
  if (!data) return <LoadingSpinner />;
  
  return <DataContent data={data} />;
}
```

---

## 6. Performance Optimization {#performance}

### Memoization
- [ ] Use React.memo for expensive components that receive same props
- [ ] Use useMemo for expensive computations
- [ ] Use useCallback for functions passed as props
- [ ] Don't over-optimize (profile first)
- [ ] Avoid inline object/array creation in props

**Examples:**
```typescript
// ❌ BAD - Inline object creation causes re-render
function Parent() {
  return <Child config={{ theme: 'dark' }} />;
}

// ✅ GOOD - Memoized config
function Parent() {
  const config = useMemo(() => ({ theme: 'dark' }), []);
  return <Child config={config} />;
}

// ✅ GOOD - React.memo for expensive component
interface ExpensiveListProps {
  items: Item[];
  onItemClick: (id: string) => void;
}

export const ExpensiveList = React.memo<ExpensiveListProps>(
  ({ items, onItemClick }) => {
    return (
      <ul>
        {items.map(item => (
          <li key={item.id} onClick={() => onItemClick(item.id)}>
            {item.name}
          </li>
        ))}
      </ul>
    );
  },
  (prevProps, nextProps) => {
    // Custom comparison function
    return (
      prevProps.items === nextProps.items &&
      prevProps.onItemClick === nextProps.onItemClick
    );
  }
);

// ✅ GOOD - useMemo for expensive computation
function DataAnalysis({ data }: { data: number[] }) {
  const statistics = useMemo(() => {
    // Expensive computation
    return {
      mean: calculateMean(data),
      median: calculateMedian(data),
      stdDev: calculateStdDev(data)
    };
  }, [data]);

  return <div>Mean: {statistics.mean}</div>;
}
```

---

## 7. Accessibility & Internationalization {#accessibility-i18n}

### Semantic Markup and ARIA
- [ ] Prefer semantic HTML elements (`button`, `nav`, `header`) over generic `div`/`span` for interactive UI
- [ ] Supply accessible names via `aria-label`, `aria-labelledby`, or visible text for custom controls
- [ ] Ensure focus order matches visual order and manage focus when dialogs/overlays open or close
- [ ] Do not use `role`/`aria-*` attributes to mask poor DOM structure; fix the markup first
- [ ] Provide `aria-live` regions for async content (loading states, background updates) where necessary

**Examples:**
```tsx
// ❌ BAD - Clickable div with no semantics or focus
export function IconButton({ onClick }: { onClick: () => void }) {
  return <div onClick={onClick}>⚙</div>;
}

// ✅ GOOD - Semantic button with accessible name
export function IconButton({ onClick }: { onClick: () => void }) {
  return (
    <button type="button" onClick={onClick} aria-label="Settings">
      <SettingsIcon aria-hidden="true" />
    </button>
  );
}

// ✅ GOOD - Focus trap for modal dialog
import FocusLock from 'react-focus-lock';

export function ConfirmDialog({ open, onClose }: Props) {
  if (!open) return null;
  return (
    <FocusLock>
      <div role="dialog" aria-modal="true" aria-labelledby="confirm-title">
        <h2 id="confirm-title">Delete item?</h2>
        {/* ... */}
        <button onClick={onClose}>Cancel</button>
      </div>
    </FocusLock>
  );
}
```

### Keyboard Interaction and Color Contrast
- [ ] All interactive elements are reachable via keyboard (`Tab`, `Shift+Tab`, arrow keys where applicable)
- [ ] Ensure visible focus indicators meet WCAG contrast requirements (3:1 ratio minimum)
- [ ] Avoid disabling focus outlines without providing an accessible replacement
- [ ] Provide skip links for long navigation menus when appropriate

**Examples:**
```tsx
// ❌ BAD - Removing focus outline with no alternative
const StyledButton = styled.button`
  outline: none;
`;

// ✅ GOOD - Custom focus ring with sufficient contrast
const StyledButton = styled.button`
  outline: none;
  &:focus-visible {
    box-shadow: 0 0 0 3px #fff, 0 0 0 5px #1d4ed8;
  }
`;
```

### Internationalization and Localization
- [ ] Use a localization framework (react-intl, i18next, FormatJS) instead of hard-coded text
- [ ] Extract user-facing strings to translation files and provide interpolation placeholders with context
- [ ] Format dates, numbers, and currencies using locale-aware APIs (`Intl.DateTimeFormat`, `Intl.NumberFormat`)
- [ ] Ensure layout can adapt to RTL languages and long translations (avoid fixed widths)
- [ ] Never concatenate translated strings—use structured messages with placeholders

**Examples:**
```tsx
// ❌ BAD - Hard-coded English string and date
return <p>{`Welcome ${user.name}, today is ${new Date().toLocaleDateString()}`}</p>;

// ✅ GOOD - Using react-intl for translation and formatting
import { useIntl, FormattedDate } from 'react-intl';

export function WelcomeBanner({ user }: { user: User }) {
  const intl = useIntl();
  return (
    <p>
      {intl.formatMessage(
        { id: 'welcome.message', defaultMessage: 'Welcome {name}, today is {date}' },
        {
          name: user.name,
          date: <FormattedDate value={new Date()} weekday="long" year="numeric" month="long" day="numeric" />,
        }
      )}
    </p>
  );
}
```

### Safe HTML and Dynamic Content
- [ ] Avoid `dangerouslySetInnerHTML`; if required, sanitize input with a trusted library (DOMPurify) and document the data source
- [ ] Escape user-generated content before rendering; never trust backend-supplied HTML without sanitization
- [ ] For markdown/HTML renderers, use allowlists for tags/attributes and strip scripts/styles
- [ ] Provide fallbacks when fonts/icons fail to load to keep text readable

**Examples:**
```tsx
// ❌ BAD - Rendering server HTML with no sanitization
<div dangerouslySetInnerHTML={{ __html: props.articleBody }} />

// ✅ GOOD - Sanitizing before rendering
import DOMPurify from 'dompurify';

export function ArticleBody({ html }: { html: string }) {
  const sanitized = useMemo(() => DOMPurify.sanitize(html, { USE_PROFILES: { html: true } }), [html]);
  return <div dangerouslySetInnerHTML={{ __html: sanitized }} />;
}
```

---

## 8. Testing Strategy {#testing}

### React Testing Library & Jest
- [ ] Prefer React Testing Library (RTL) for component/unit tests to exercise behavior, not implementation details
- [ ] Query elements using accessible roles/text (`screen.getByRole`, `getByText`) instead of brittle selectors
- [ ] Use `userEvent` to simulate real user interactions and await async updates with `findBy*`/`waitFor`
- [ ] Keep tests deterministic by mocking timers/network calls and cleaning up after each test
- [ ] Avoid snapshot-only coverage; assert on observable behavior instead

**Examples:**
```tsx
// ❌ BAD - Testing implementation details and snapshot-only
const { container, instance } = render(<Counter />);
expect(instance.state.count).toBe(0);
expect(container).toMatchSnapshot();

// ✅ GOOD - Testing behavior via RTL
import { render, screen } from '@testing-library/react';
import userEvent from '@testing-library/user-event';

test('increments count when button clicked', async () => {
  render(<Counter />);
  await userEvent.click(screen.getByRole('button', { name: /increment/i }));
  expect(screen.getByText(/count: 1/i)).toBeInTheDocument();
});
```

### Mocking Data Fetching and Side Effects
- [ ] Mock HTTP clients/fetch requests (MSW, jest-fetch-mock, Axios mocks) to avoid real network calls
- [ ] Use MSW or Storybook mock handlers to keep tests close to production behavior
- [ ] Assert error states (timeouts, 500s) in addition to happy path
- [ ] Clean up spies/mocks between tests (`afterEach(jest.resetAllMocks)`)

**Examples:**
```tsx
import { rest } from 'msw';
import { setupServer } from 'msw/node';

const server = setupServer(
  rest.get('/api/users/:id', (req, res, ctx) => {
    return res(ctx.json({ id: req.params.id, name: 'Jane' }));
  })
);

beforeAll(() => server.listen());
afterEach(() => server.resetHandlers());
afterAll(() => server.close());

test('renders user name from API', async () => {
  render(<UserProfile userId="123" />);
  expect(await screen.findByText(/jane/i)).toBeInTheDocument();
});
```

### Component Variants, Storybook, and Visual Regression
- [ ] Maintain Storybook stories (or equivalent) for complex components to preview different states
- [ ] Use interaction tests (`play` functions or Storybook Testing Library) for UI flows that cross components
- [ ] Run visual regression tests (Chromatic/Backstop) for high-risk styling changes, especially around accessibility adjustments

### End-to-End and Integration Signals
- [ ] Ensure Cypress/Playwright suites cover critical user funnels impacted by React changes
- [ ] Gate asynchronous logic with test IDs or aria attributes only when necessary and documented
- [ ] When adding hooks/context logic, include integration tests that render the provider tree (not just isolated hook tests)

---

## 9. Resiliency, Suspense, and Code Splitting {#resiliency}

### Error Boundaries
- [ ] Wrap asynchronous component trees (lazy-loaded routes, data fetching shells) in an `ErrorBoundary`
- [ ] Provide user-friendly fallback UIs with retry/feedback actions
- [ ] Log error boundary failures to observability tooling (Sentry, Datadog) with context
- [ ] Avoid throwing non-Error objects; standardize on `Error` subclasses for predictable handling

**Examples:**
```tsx
// ✅ GOOD - Reusable error boundary
class RouteErrorBoundary extends React.Component<Props, State> {
  state = { hasError: false };

  static getDerivedStateFromError() {
    return { hasError: true };
  }

  componentDidCatch(error: Error, info: React.ErrorInfo) {
    logClientError(error, info);
  }

  render() {
    if (this.state.hasError) {
      return (
        <ErrorState
          title="Something went wrong"
          onRetry={() => this.setState({ hasError: false })}
        />
      );
    }
    return this.props.children;
  }
}
```

### Suspense and Data Fetching
- [ ] Use `React.Suspense` with appropriate fallbacks for lazy components and data libraries (React Query, Relay)
- [ ] Ensure Suspense fallbacks do not block critical page content indefinitely
- [ ] Combine Suspense with `useTransition`/`startTransition` when deferring low-priority updates
- [ ] Handle rejected promises from data loaders; do not rely solely on Suspense for error cases

**Examples:**
```tsx
const UserProfile = React.lazy(() => import('./UserProfile'));

export function Dashboard() {
  return (
    <RouteErrorBoundary>
      <React.Suspense fallback={<Spinner label="Loading profile" />}>
        <UserProfile />
      </React.Suspense>
    </RouteErrorBoundary>
  );
}
```

### Code Splitting and Lazy Loading
- [ ] Use dynamic imports (`React.lazy`, `next/dynamic`, `loadable-components`) for large routes/widgets to reduce initial bundle size
- [ ] Preload critical chunks when the user is likely to need them (prefetch on hover/in viewport)
- [ ] Ensure lazy-loaded components still enforce authentication/authorization checks
- [ ] Avoid waterfalls by grouping related imports or using `Promise.all`

**Examples:**
```tsx
// ✅ GOOD - Route-based code splitting with prefetch
const ReportsPage = React.lazy(() => import('./ReportsPage'));

function AppRouter() {
  return (
    <Routes>
      <Route
        path="/reports"
        element={
          <React.Suspense fallback={<PageSkeleton />}>
            <ReportsPage />
          </React.Suspense>
        }
      />
    </Routes>
  );
}

// Prefetch when link becomes visible
useEffect(() => {
  const controller = new AbortController();
  import('./ReportsPage');
  return () => controller.abort();
}, []);
```

### Network Resiliency
- [ ] Surface retry/backoff UI for failed HTTP calls (especially mutations)
- [ ] Cancel in-flight requests on component unmount to avoid updating unmounted components
- [ ] Cache data locally (React Query/SWR) to avoid refetch storms during transitions
- [ ] Validate that offline/slow-network states render meaningful messaging

---

## Review Checklist Summary

Quick checklist for React/TypeScript code reviews:

- [ ] **TypeScript**: No `any` without justification, proper type annotations, strict mode enabled
- [ ] **Hooks**: Proper dependency arrays, custom hooks follow rules, cleanup in effects
- [ ] **Components**: Functional components with typed props, proper composition
- [ ] **State**: Appropriate use of useState/useEffect/Context, no derived state
- [ ] **HTTP**: Timeouts configured, AbortController used, proper error handling
- [ ] **Performance**: Appropriate memoization, avoid unnecessary re-renders
- [ ] **Accessibility/i18n**: Semantic markup, keyboard/focus handling, localized strings, safe HTML usage
- [ ] **Testing**: Behavior-focused RTL/Jest coverage with mocked data sources and documented Storybook/E2E scenarios
- [ ] **Resiliency**: Error boundaries, Suspense fallbacks, code splitting, and retry/cancellation patterns in place

---

## References

- [React TypeScript Cheatsheet](https://react-typescript-cheatsheet.netlify.app/)
- [React Hooks Documentation](https://react.dev/reference/react)
- [TypeScript Handbook](https://www.typescriptlang.org/docs/handbook/intro.html)
- [React Best Practices](https://react.dev/learn)
